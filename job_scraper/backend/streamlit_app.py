"""
Streamlit application for job scraper with visualization
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime, timedelta
import schedule
import time
from scraper import JobScraper
from config import JOB_CATEGORIES, JOB_TYPES
import json
import os
import folium
from streamlit_folium import st_folium
from collections import Counter


# Page configuration
st.set_page_config(
    page_title="Arbeitsagentur Job Scraper",
    page_icon="📊",
    layout="wide"
)


class StreamlitJobApp:
    def __init__(self):
        self.scraper = JobScraper()
        
        # Initialize session state
        if 'job_categories' not in st.session_state:
            st.session_state.job_categories = JOB_CATEGORIES.copy()
        if 'last_scrape' not in st.session_state:
            st.session_state.last_scrape = None
    
    def render_sidebar(self):
        """Render sidebar with controls"""
        st.sidebar.title("⚙️ Einstellungen")
        
        # Job categories management
        st.sidebar.subheader("Berufsfelder verwalten")
        
        # Add new category
        new_category = st.sidebar.text_input("Neues Berufsfeld hinzufügen")
        if st.sidebar.button("➕ Hinzufügen") and new_category:
            if new_category not in st.session_state.job_categories:
                st.session_state.job_categories.append(new_category)
                st.sidebar.success(f"'{new_category}' hinzugefügt!")
                st.rerun()
            else:
                st.sidebar.warning("Berufsfeld existiert bereits!")
        
        # Display and manage categories
        st.sidebar.subheader("Aktuelle Berufsfelder")
        categories_to_remove = []
        
        for i, category in enumerate(st.session_state.job_categories):
            col1, col2 = st.sidebar.columns([3, 1])
            col1.write(f"• {category}")
            if col2.button("🗑️", key=f"remove_{i}"):
                categories_to_remove.append(category)
        
        # Remove selected categories
        for category in categories_to_remove:
            st.session_state.job_categories.remove(category)
            st.rerun()
        
        st.sidebar.divider()
        
        # Scraping controls
        st.sidebar.subheader("Scraping Steuerung")
        
        if st.sidebar.button("🔄 Jetzt scrapen", type="primary"):
            try:
                with st.spinner("Scraping läuft... Dies kann einige Minuten dauern."):
                    results = self.scraper.scrape_all_categories(st.session_state.job_categories)
                    if results:
                        self.scraper.save_results(results)
                        st.session_state.last_scrape = datetime.now()
                        st.sidebar.success(f"✅ Scraping abgeschlossen! {len(results)} Einträge gespeichert.")
                        st.rerun()
                    else:
                        st.sidebar.error("❌ Scraping fehlgeschlagen. Keine Daten erhalten.")
            except Exception as e:
                st.sidebar.error(f"❌ Fehler beim Scraping: {str(e)}")
                st.sidebar.info("Bitte überprüfen Sie Ihre Internetverbindung und versuchen Sie es erneut.")
        
        if st.session_state.last_scrape:
            st.sidebar.info(f"Letztes Scraping: {st.session_state.last_scrape.strftime('%d.%m.%Y %H:%M')}")
    
    def plot_matplotlib_bar_chart(self, df, job_type):
        """Create bar chart using matplotlib"""
        # Filter data for specific job type
        df_filtered = df[df['job_type'] == job_type].groupby('category')['count'].mean().sort_values(ascending=False)
        
        # Show data table
        st.subheader(f"📊 Daten für {job_type}")
        data_display = df_filtered.reset_index()
        data_display.columns = ['Berufsfeld', 'Durchschnittliche Anzahl']
        data_display['Durchschnittliche Anzahl'] = data_display['Durchschnittliche Anzahl'].round(1)
        st.dataframe(data_display, use_container_width=True)
        
        # Create chart
        fig, ax = plt.subplots(figsize=(12, 6))
        
        colors = plt.cm.viridis(range(len(df_filtered)))
        bars = ax.bar(df_filtered.index, df_filtered.values, color=colors)
        
        ax.set_xlabel('Berufsfeld', fontsize=12, fontweight='bold')
        ax.set_ylabel('Durchschnittliche Anzahl Stellenangebote', fontsize=12, fontweight='bold')
        ax.set_title(f'Stellenangebote nach Berufsfeld - {job_type}', fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        return fig
    
    def plot_plotly_bar_chart(self, df, job_type):
        """Create interactive bar chart using plotly"""
        df_filtered = df[df['job_type'] == job_type].groupby('category')['count'].mean().reset_index()
        df_filtered = df_filtered.sort_values('count', ascending=False)
        
        # Show data table
        st.subheader(f"📊 Daten für {job_type}")
        data_display = df_filtered.copy()
        data_display.columns = ['Berufsfeld', 'Durchschnittliche Anzahl']
        data_display['Durchschnittliche Anzahl'] = data_display['Durchschnittliche Anzahl'].round(1)
        st.dataframe(data_display, use_container_width=True)
        
        # Create chart
        fig = px.bar(
            df_filtered,
            x='category',
            y='count',
            title=f'Stellenangebote nach Berufsfeld - {job_type}',
            labels={'category': 'Berufsfeld', 'count': 'Durchschnittliche Anzahl'},
            color='count',
            color_continuous_scale='Viridis',
            text='count'
        )
        
        fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500,
            showlegend=False
        )
        
        return fig
    
    def plot_time_series(self, df, category):
        """Create time series plot for a specific category"""
        df_filtered = df[df['category'] == category].copy()
        df_filtered['date'] = pd.to_datetime(df_filtered['date'])
        
        fig = px.line(
            df_filtered,
            x='date',
            y='count',
            color='job_type',
            title=f'Zeitverlauf - {category}',
            labels={'date': 'Datum', 'count': 'Anzahl Stellenangebote', 'job_type': 'Angebotsart'},
            markers=True
        )
        
        fig.update_layout(height=400)
        return fig
    
    def render_main_content(self):
        """Render main content area"""
        st.title("📊 Arbeitsagentur Job Scraper Dashboard")
        st.markdown("---")
        
        # Load data
        df = self.scraper.load_history()
        
        if df.empty:
            st.warning("⚠️ Keine Daten vorhanden. Bitte führen Sie ein Scraping durch.")
            return
        
        # Convert date column
        df['date'] = pd.to_datetime(df['date'])
        
        # Summary statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Berufsfelder", len(st.session_state.job_categories))
        with col2:
            st.metric("Angebotsarten", len(JOB_TYPES))
        with col3:
            total_jobs = df[df['date'] == df['date'].max()]['count'].sum()
            st.metric("Aktuelle Stellenangebote", f"{total_jobs:,}")
        with col4:
            st.metric("Datenpunkte", len(df))
        
        st.markdown("---")
        
        # Visualization tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Bar Charts (Matplotlib)",
            "📈 Bar Charts (Plotly)",
            "📉 Zeitverlauf",
            "🗺️ Deutschland Heatmap",
            "🏢 Unternehmen-Analyse"
        ])
        
        with tab1:
            st.subheader("Bar Charts - Matplotlib")
            
            for job_type in JOB_TYPES.keys():
                st.markdown(f"### {job_type}")
                fig = self.plot_matplotlib_bar_chart(df, job_type)
                st.pyplot(fig)
                plt.close()
        
        with tab2:
            st.subheader("Interaktive Bar Charts - Plotly Express")
            
            for job_type in JOB_TYPES.keys():
                st.markdown(f"### {job_type}")
                fig = self.plot_plotly_bar_chart(df, job_type)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.subheader("Zeitverlauf nach Berufsfeld")
            
            selected_category = st.selectbox(
                "Berufsfeld auswählen",
                options=st.session_state.job_categories
            )
            
            if selected_category:
                fig = self.plot_time_series(df, selected_category)
                st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            self.render_heatmap()
        
        with tab5:
            self.render_companies_analysis()
        
        # Data table
        st.markdown("---")
        st.subheader("📋 Rohdaten")
        
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            selected_job_type = st.multiselect(
                "Angebotsart filtern",
                options=df['job_type'].unique(),
                default=df['job_type'].unique()
            )
        with col2:
            selected_categories = st.multiselect(
                "Berufsfelder filtern",
                options=df['category'].unique(),
                default=df['category'].unique()
            )
        
        # Apply filters
        df_display = df[
            (df['job_type'].isin(selected_job_type)) &
            (df['category'].isin(selected_categories))
        ].sort_values('date', ascending=False)
        
        st.dataframe(df_display, use_container_width=True)
        
        # Download button
        csv = df_display.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Daten als CSV herunterladen",
            data=csv,
            file_name=f"job_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    def render_heatmap(self):
        """Render Germany heatmap with job locations"""
        st.subheader("🗺️ Stellenangebote in Deutschland - Heatmap")
        
        locations = self.scraper.load_locations_data()
        
        if not locations:
            st.info("Keine Standortdaten vorhanden. Führen Sie ein detailliertes Scraping durch.")
            if st.button("🔍 Detailliertes Scraping starten"):
                with st.spinner("Detailliertes Scraping läuft... Dies kann länger dauern."):
                    jobs = self.scraper.scrape_all_detailed(st.session_state.job_categories, max_per_category=50)
                    self.scraper.save_detailed_data(jobs)
                    st.success(f"✅ {len(jobs)} detaillierte Jobs gescraped!")
                    st.rerun()
            return
        
        # Create map centered on Germany
        m = folium.Map(
            location=[51.1657, 10.4515],  # Center of Germany
            zoom_start=6,
            tiles='OpenStreetMap'
        )
        
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            selected_job_types = st.multiselect(
                "Angebotsart filtern",
                options=list(JOB_TYPES.keys()),
                default=list(JOB_TYPES.keys())
            )
        with col2:
            selected_categories = st.multiselect(
                "Berufsfelder filtern",
                options=list(set([loc['category'] for loc in locations])),
                default=list(set([loc['category'] for loc in locations]))
            )
        
        # Filter locations
        filtered_locations = [
            loc for loc in locations
            if loc['job_type'] in selected_job_types and loc['category'] in selected_categories
        ]
        
        # Add markers
        for loc in filtered_locations:
            folium.CircleMarker(
                location=[loc['lat'], loc['lon']],
                radius=5,
                popup=f"<b>{loc['company']}</b><br>{loc['city']}<br>{loc['category']}",
                color='red',
                fill=True,
                fillColor='red',
                fillOpacity=0.6
            ).add_to(m)
        
        # Display map
        st_folium(m, width=1200, height=600)
        
        # Statistics
        st.markdown("### 📊 Standort-Statistiken")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Standorte gesamt", len(filtered_locations))
        with col2:
            unique_cities = len(set([loc['city'] for loc in filtered_locations]))
            st.metric("Städte", unique_cities)
        with col3:
            unique_companies = len(set([loc['company'] for loc in filtered_locations]))
            st.metric("Unternehmen", unique_companies)
    
    def render_companies_analysis(self):
        """Render companies/keywords analysis with CRUD"""
        st.subheader("🏢 Unternehmen-Analyse")
        
        companies_data = self.scraper.load_companies_data()
        
        if not companies_data:
            st.info("Keine Unternehmensdaten vorhanden. Führen Sie ein detailliertes Scraping durch.")
            if st.button("🔍 Detailliertes Scraping starten", key="companies_scrape"):
                with st.spinner("Detailliertes Scraping läuft..."):
                    jobs = self.scraper.scrape_all_detailed(st.session_state.job_categories, max_per_category=50)
                    self.scraper.save_detailed_data(jobs)
                    st.success(f"✅ {len(jobs)} detaillierte Jobs gescraped!")
                    st.rerun()
            return
        
        # Select job type
        selected_job_type = st.selectbox(
            "Angebotsart auswählen",
            options=list(companies_data.keys())
        )
        
        if selected_job_type not in companies_data:
            st.warning("Keine Daten für diese Angebotsart")
            return
        
        companies = companies_data[selected_job_type]
        
        # Display options
        col1, col2 = st.columns([3, 1])
        with col1:
            show_count = st.slider("Anzahl anzeigen", 5, 50, 20)
        with col2:
            sort_order = st.radio("Sortierung", ["Absteigend", "Aufsteigend"])
        
        # Sort companies
        if sort_order == "Aufsteigend":
            companies = sorted(companies, key=lambda x: x['count'])
        else:
            companies = sorted(companies, key=lambda x: x['count'], reverse=True)
        
        # Display top companies
        st.markdown(f"### Top {show_count} Unternehmen - {selected_job_type}")
        
        # Create DataFrame
        df_companies = pd.DataFrame(companies[:show_count])
        
        # Add visibility column if not exists
        if 'visible' not in df_companies.columns:
            df_companies['visible'] = True
        
        # Display table with checkboxes
        for idx, row in df_companies.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**{row['name']}**")
            with col2:
                st.write(f"{row['count']} Stellen")
            with col3:
                visible = st.checkbox(
                    "Anzeigen",
                    value=row.get('visible', True),
                    key=f"vis_{selected_job_type}_{idx}"
                )
                if visible != row.get('visible', True):
                    self.scraper.update_company_visibility(
                        selected_job_type,
                        row['name'],
                        visible
                    )
        
        # Bar chart
        st.markdown("### 📊 Visualisierung")
        visible_companies = df_companies[df_companies.get('visible', True) == True]
        
        if not visible_companies.empty:
            fig = px.bar(
                visible_companies,
                x='name',
                y='count',
                title=f'Top Unternehmen - {selected_job_type}',
                labels={'name': 'Unternehmen', 'count': 'Anzahl Stellenangebote'},
                color='count',
                color_continuous_scale='Viridis'
            )
            fig.update_layout(xaxis_tickangle=-45, height=500)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Keine sichtbaren Unternehmen ausgewählt")
        
        # Export functionality
        if st.button("📥 Unternehmensdaten exportieren"):
            csv = df_companies.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="CSV herunterladen",
                data=csv,
                file_name=f"companies_{selected_job_type}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    def run(self):
        """Run the Streamlit app"""
        self.render_sidebar()
        self.render_main_content()


def main():
    app = StreamlitJobApp()
    app.run()


if __name__ == "__main__":
    main()

# Made with Bob

    
    def render_heatmap(self):
        """Render Germany heatmap with job locations"""
        st.subheader("🗺️ Stellenangebote in Deutschland - Heatmap")
        
        locations = self.scraper.load_locations_data()
        
        if not locations:
            st.info("Keine Standortdaten vorhanden. Führen Sie ein detailliertes Scraping durch.")
            if st.button("🔍 Detailliertes Scraping starten"):
                with st.spinner("Detailliertes Scraping läuft... Dies kann länger dauern."):
                    jobs = self.scraper.scrape_all_detailed(st.session_state.job_categories, max_per_category=50)
                    self.scraper.save_detailed_data(jobs)
                    st.success(f"✅ {len(jobs)} detaillierte Jobs gescraped!")
                    st.rerun()
            return
        
        # Create map centered on Germany
        m = folium.Map(
            location=[51.1657, 10.4515],  # Center of Germany
            zoom_start=6,
            tiles='OpenStreetMap'
        )
        
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            selected_job_types = st.multiselect(
                "Angebotsart filtern",
                options=list(JOB_TYPES.keys()),
                default=list(JOB_TYPES.keys())
            )
        with col2:
            selected_categories = st.multiselect(
                "Berufsfelder filtern",
                options=list(set([loc['category'] for loc in locations])),
                default=list(set([loc['category'] for loc in locations]))
            )
        
        # Filter locations
        filtered_locations = [
            loc for loc in locations
            if loc['job_type'] in selected_job_types and loc['category'] in selected_categories
        ]
        
        # Add markers
        for loc in filtered_locations:
            folium.CircleMarker(
                location=[loc['lat'], loc['lon']],
                radius=5,
                popup=f"<b>{loc['company']}</b><br>{loc['city']}<br>{loc['category']}",
                color='red',
                fill=True,
                fillColor='red',
                fillOpacity=0.6
            ).add_to(m)
        
        # Display map
        st_folium(m, width=1200, height=600)
        
        # Statistics
        st.markdown("### 📊 Standort-Statistiken")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Standorte gesamt", len(filtered_locations))
        with col2:
            unique_cities = len(set([loc['city'] for loc in filtered_locations]))
            st.metric("Städte", unique_cities)
        with col3:
            unique_companies = len(set([loc['company'] for loc in filtered_locations]))
            st.metric("Unternehmen", unique_companies)
    
    def render_companies_analysis(self):
        """Render companies/keywords analysis with CRUD"""
        st.subheader("🏢 Unternehmen-Analyse")
        
        companies_data = self.scraper.load_companies_data()
        
        if not companies_data:
            st.info("Keine Unternehmensdaten vorhanden. Führen Sie ein detailliertes Scraping durch.")
            if st.button("🔍 Detailliertes Scraping starten", key="companies_scrape"):
                with st.spinner("Detailliertes Scraping läuft..."):
                    jobs = self.scraper.scrape_all_detailed(st.session_state.job_categories, max_per_category=50)
                    self.scraper.save_detailed_data(jobs)
                    st.success(f"✅ {len(jobs)} detaillierte Jobs gescraped!")
                    st.rerun()
            return
        
        # Select job type
        selected_job_type = st.selectbox(
            "Angebotsart auswählen",
            options=list(companies_data.keys())
        )
        
        if selected_job_type not in companies_data:
            st.warning("Keine Daten für diese Angebotsart")
            return
        
        companies = companies_data[selected_job_type]
        
        # Display options
        col1, col2 = st.columns([3, 1])
        with col1:
            show_count = st.slider("Anzahl anzeigen", 5, 50, 20)
        with col2:
            sort_order = st.radio("Sortierung", ["Absteigend", "Aufsteigend"])
        
        # Sort companies
        if sort_order == "Aufsteigend":
            companies = sorted(companies, key=lambda x: x['count'])
        else:
            companies = sorted(companies, key=lambda x: x['count'], reverse=True)
        
        # Display top companies
        st.markdown(f"### Top {show_count} Unternehmen - {selected_job_type}")
        
        # Create DataFrame
        df_companies = pd.DataFrame(companies[:show_count])
        
        # Add visibility column if not exists
        if 'visible' not in df_companies.columns:
            df_companies['visible'] = True
        
        # Display table with checkboxes
        for idx, row in df_companies.iterrows():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**{row['name']}**")
            with col2:
                st.write(f"{row['count']} Stellen")
            with col3:
                visible = st.checkbox(
                    "Anzeigen",
                    value=row.get('visible', True),
                    key=f"vis_{selected_job_type}_{idx}"
                )
                if visible != row.get('visible', True):
                    self.scraper.update_company_visibility(
                        selected_job_type,
                        row['name'],
                        visible
                    )
        
        # Bar chart
        st.markdown("### 📊 Visualisierung")
        visible_companies = df_companies[df_companies.get('visible', True) == True]
        
        if not visible_companies.empty:
            fig = px.bar(
                visible_companies,
                x='name',
                y='count',
                title=f'Top Unternehmen - {selected_job_type}',
                labels={'name': 'Unternehmen', 'count': 'Anzahl Stellenangebote'},
                color='count',
                color_continuous_scale='Viridis'
            )
            fig.update_layout(xaxis_tickangle=-45, height=500)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Keine sichtbaren Unternehmen ausgewählt")
        
        # Export functionality
        if st.button("📥 Unternehmensdaten exportieren"):
            csv = df_companies.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="CSV herunterladen",
                data=csv,
                file_name=f"companies_{selected_job_type}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
