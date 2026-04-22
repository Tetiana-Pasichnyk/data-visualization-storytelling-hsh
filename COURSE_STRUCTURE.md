# Data Visualization & Storytelling
## Hochschule Hannover (HsH)

**Course Type:** Elective  
**ECTS:** 5  
**Semester:** 4-6  
**Language:** German  
**Format:** In-person with practical exercises  
**Created:** April 2026

---

## 📋 Course Description

This course teaches the ability to visualize data convincingly and communicate data-driven recommendations professionally. Students learn to work with modern visualization tools, create accessible graphics, and tell complex data stories.

### Why This Course?

In a data-driven world, the ability to visually prepare and communicate information is crucial. This course combines:
- **Technical Skills:** Python libraries (Matplotlib, Seaborn, Plotly)
- **Design Principles:** Edward Tufte, WCAG standards, Accessibility
- **Communication:** Storytelling, presentation techniques
- **Practice:** Real datasets, interactive dashboards, BI tools

---

## 🎯 Learning Objectives

After successful completion, students can:

### Technical Competencies
1. ✓ Create professional visualizations with Python (Matplotlib, Seaborn, Plotly)
2. ✓ Develop interactive dashboards (Streamlit, Bokeh)
3. ✓ Integrate various data sources (CSV, JSON, SQL, APIs)
4. ✓ Use BI tools fundamentally (Power BI, Tableau)

### Design Competencies
5. ✓ Apply Tufte principles (Data-Ink Ratio, avoid Chartjunk)
6. ✓ Create accessible visualizations (WCAG 2.1 AA/AAA)
7. ✓ Consider color blindness (Okabe-Ito, Paul Tol palettes)
8. ✓ Choose appropriate visualization types for different data types

### Conceptual Competencies
9. ✓ Tell data-driven stories
10. ✓ Communicate appropriately for target audiences
11. ✓ Critically evaluate and improve visualizations
12. ✓ Understand ethical aspects of data visualization

---

## 📚 Course Structure

The course consists of **9 teaching blocks** (1 day each) with **2-3 units** (90 minutes each).

### Block 1: Introduction & Fundamentals
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Orientation, setup, first visualizations

**Learning Objectives:**
- Understand visualization landscape
- Set up development environment
- Create first plots with Matplotlib
- Use data sources (Kaggle, CSV, JSON)

### Block 2: Data Representations & Seaborn I
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Matplotlib basics, Seaborn introduction

**Learning Objectives:**
- Understand Matplotlib Figure-Axes architecture
- Use Seaborn for statistical plots
- Choose scales correctly (linear, logarithmic)
- Visualize statistical metrics

### Block 3: Focus I - Specialized Visualizations
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Advanced techniques, Tufte principles

**Learning Objectives:**
- Create complex layouts (Subplots, Grids)
- Use specialized plot types (Pairplot, Heatmap)
- Apply Tufte principles
- Analyze real data

### Block 4: Plotly I & Bokeh
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Interactive visualizations

**Learning Objectives:**
- Understand and use interactivity
- Use Plotly Express
- Create Bokeh plots
- Export HTML visualizations

### Block 5: Accessibility I - Best Practices
**Duration:** 1 day (270 min = 3 units)  
**Focus:** WCAG standards, inclusive design

**Learning Objectives:**
- Apply WCAG 2.1 standards (AA/AAA)
- Consider color blindness
- Test contrast ratios
- Create accessible visualizations

### Block 6: Storytelling I
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Narrative structures, communication

**Learning Objectives:**
- Understand storytelling principles
- Apply narrative structures
- Communicate appropriately for target audiences
- Master presentation techniques

### Block 7: Research I
**Duration:** 1 day (270 min = 3 units)  
**Focus:** ML visualization, EDA

**Learning Objectives:**
- Visualize ML metrics (Confusion Matrix, ROC)
- Reduce high-dimensional data (t-SNE, UMAP)
- Perform EDA
- Create research visualizations

### Block 8: Dashboard I
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Dashboard design, Streamlit

**Learning Objectives:**
- Understand dashboard principles
- Use Streamlit
- Create interactive dashboards
- Deploy dashboards

### Block 9: Advanced Tools II
**Duration:** 1 day (270 min = 3 units)  
**Focus:** Power BI, advanced techniques

**Learning Objectives:**
- Use Power BI fundamentally
- Master Seaborn
- Create Dash apps
- Produce professional visualizations

**Detailed block descriptions:** See [BLOCKS_SUMMARY.md](BLOCKS_SUMMARY.md)

---

## 🗓️ Time Planning Options

The course is modular and can be offered in different formats:

### Option 1: Full Semester (recommended)
- **Duration:** 11 weeks
- **Format:** 1 block per week
- **Effort:** ~15 hours/week (incl. assignments)
- **Total:** ~150 hours

### Option 2: Intensive Course
- **Duration:** 4 weeks
- **Format:** 3 blocks per week
- **Effort:** ~30 hours/week
- **Total:** ~120 hours

### Option 3: Weekend Workshop
- **Duration:** 4 weekends
- **Format:** 2-3 blocks per weekend
- **Effort:** ~25 hours/weekend
- **Total:** ~100 hours

**Full details:** See [`optional/MODULARITAET.md`](optional/MODULARITAET.md)

---

## 📋 Prerequisites

### Technical Prerequisites
- **Programming:** Basic Python knowledge (variables, functions, lists, dictionaries)
- **Mathematics:** Basic statistics (mean, median, standard deviation)
- **Optional:** Pandas basics, NumPy basics (reviewed in course)

### Hardware & Software
- **Laptop:** Windows, macOS or Linux
- **RAM:** Minimum 8 GB (16 GB recommended)
- **Python:** Version 3.8 or higher
- **Internet:** Stable connection for online tools

---

## 🔧 Technical Requirements

### Python Installation

```bash
# Anaconda (recommended)
conda create -n dataviz python=3.10
conda activate dataviz

# Core libraries
pip install matplotlib seaborn plotly pandas numpy jupyter
```

### Alternative: Google Colab
- Free: https://colab.research.google.com
- No installation needed
- All libraries pre-installed

---

## 📊 Assessment

### Overview
- **Weekly Assignments:** 60% (9 assignments × 6-7%)
- **Final Project:** 40%

### Weekly Assignments (60%)
**Format:** Jupyter Notebook + Documentation  
**Submission:** 1 week after respective block  
**Scope:** 2-4 hours work time

**Grading Criteria:**
- Technical Implementation (40%)
- Visual Design (30%)
- Documentation (20%)
- Creativity (10%)

### Final Project (40%)
**Scope:** Complete data visualization story  
**Duration:** 2 weeks  
**Presentation:** 15 minutes + 5 minutes Q&A

**Requirements:**
- Own dataset (Kaggle, own data, public APIs)
- At least 5-7 different visualizations
- Interactive dashboard (Streamlit or similar)
- Storytelling narrative
- WCAG AA compliant
- Complete documentation

**Full assessment details:** See [`optional/BEWERTUNG.md`](optional/BEWERTUNG.md)

---

## 🛠️ Tools & Technologies

### Primary Tools (Required)
- **Matplotlib** - Base visualizations, full control
- **Seaborn** - Statistical visualizations
- **Plotly** - Interactive plots
- **Pandas** - Data manipulation

### Secondary Tools (Optional)
- **Bokeh** - Interactive visualizations, server apps
- **Streamlit** - Rapid dashboard prototyping
- **Power BI** - Business intelligence
- **Tableau** - Enterprise visualization

**Full tool comparison:** See [`optional/TOOL_VERGLEICH.md`](optional/TOOL_VERGLEICH.md)

---

## 📖 Learning Resources

### Recommended Books
- **Edward Tufte:** "The Visual Display of Quantitative Information"
- **Cole Nussbaumer Knaflic:** "Storytelling with Data"
- **Alberto Cairo:** "The Truthful Art"

### Online Resources
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/)
- [Plotly Documentation](https://plotly.com/python/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)

---

## 🎓 Learning Paths

The course offers different learning paths for different career goals:

### Python Developer Path (6 blocks)
**Blocks:** 1, 2, 3, 4, 7, 8  
**Focus:** Programming, Automation  
**Project:** Automated reporting dashboard

### Business Analyst Path (5 blocks)
**Blocks:** 1, 2, 5, 6, 9  
**Focus:** Storytelling, BI tools  
**Project:** Business presentation with data

### Data Scientist Path (5 blocks)
**Blocks:** 1, 2, 3, 5, 7  
**Focus:** Research, ML visualization  
**Project:** ML model analysis and interpretation

### Full-Stack Path (9 blocks)
**Blocks:** 1-9 (complete)  
**Focus:** All aspects  
**Project:** Complete data story with dashboard

**Full path details:** See [`optional/MODULARITAET.md`](optional/MODULARITAET.md)

---

## 🌟 Special Features

### Modularity
- Blocks can be completed in different orders
- Adaptable to different time formats
- Various learning paths possible

### Practice-Oriented
- Real datasets (Kaggle, public data)
- Industry-relevant tools
- Project-based learning
- Portfolio building

### Accessibility
- WCAG 2.1 standards from the start
- Inclusive design principles
- Practical checklists
- Awareness for accessibility

### Storytelling
- Narrative structures
- Audience analysis
- Presentation techniques
- Communication skills

---

## 📞 Support & Communication

### Office Hours
- **When:** By appointment
- **Where:** Office or online (Zoom/Teams)
- **Topics:** Content questions, project consultation

### Online Forum
- **Platform:** Moodle/Discord/Slack
- **Usage:** Ask questions, discussions, code sharing

### Peer Learning
- **Study Groups:** 3-4 students
- **Activities:** Code review, discussions, collaborative learning

---

## 📝 Contact

**Instructor:** [Insert name]  
**Email:** [email@hsh.de]  
**Office:** [Room number]  
**Office Hours:** [Time and location]

**Course Website:** [URL]  
**Moodle:** [Course link]  
**GitHub:** [Repository link]

---

## 📚 Instructor Materials

**Detailed planning and implementation materials available in [`optional/`](optional/) folder:**
- Complete implementation plan ([`PLAN.md`](optional/PLAN.md))
- Modularity and time formats ([`MODULARITAET.md`](optional/MODULARITAET.md))
- Assessment framework ([`BEWERTUNG.md`](optional/BEWERTUNG.md))
- Tool comparison ([`TOOL_VERGLEICH.md`](optional/TOOL_VERGLEICH.md))
- Block 1 complete template ([`Block_1_Einfuehrung_Grundlagen.md`](optional/Block_1_Einfuehrung_Grundlagen.md))
- Implementation summary ([`IMPLEMENTATION_SUMMARY.md`](optional/IMPLEMENTATION_SUMMARY.md))

---

**Version:** 1.0  
**Last Updated:** April 2026  
**Status:** Active

---

*This course was developed to equip students with the most important skills for data-driven communication. Good luck!*