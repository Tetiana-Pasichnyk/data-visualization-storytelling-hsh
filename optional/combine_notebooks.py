#!/usr/bin/env python3
"""
Matplotlib Notebooks Combiner

This script programmatically combines three matplotlib notebooks into a comprehensive
teaching resource. It extracts specific cell ranges from each source notebook and
combines them into a well-structured output notebook with section headers.

Usage:
    python combine_notebooks.py --sections 1-3      # Build sections 1-3
    python combine_notebooks.py --sections 4-7      # Build sections 4-7
    python combine_notebooks.py --sections all      # Build all sections
    python combine_notebooks.py --sections 1,3,5    # Build specific sections

Author: Bob
Date: 2026-04-20
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


# Source notebook paths
SOURCE_NOTEBOOKS = {
    'kopie': 'Kopie_von_Intro_to_matplotlib.ipynb',
    'fundamentals': 'matplotlib_fundamentals_explained.ipynb',
    'video': 'introduction-to-matplotlib-video.ipynb'
}

# Output notebook path
OUTPUT_NOTEBOOK = 'matplotlib_complete_guide.ipynb'


# Section definitions based on the structure analysis
SECTIONS = {
    1: {
        'title': 'Introduction & Setup',
        'description': 'What is matplotlib, installation, imports, and your first plot',
        'duration': '15-20 minutes',
        'sources': [
            ('kopie', 0, 8, 'Introduction and basic setup'),
            ('video', 0, 2, 'Matplotlib concepts and why use it')
        ]
    },
    2: {
        'title': 'Core Concepts - Figure Architecture',
        'description': 'Understanding Figure vs Axes hierarchy, pyplot vs OO interface',
        'duration': '20-25 minutes',
        'sources': [
            ('kopie', 22, 39, 'Figures, subplots, and axes hierarchy'),
            ('fundamentals', 8, 11, 'plt.show() vs fig.show() and architecture')
        ]
    },
    3: {
        'title': 'Understanding Data for Plotting',
        'description': 'NumPy arrays, lists, linspace, and why arrays matter',
        'duration': '15-20 minutes',
        'sources': [
            ('fundamentals', 2, 2, 'np.linspace() explanation'),
            ('fundamentals', 31, 43, 'Arrays vs lists and performance'),
            ('kopie', 9, 21, 'Compatible data types')
        ]
    },
    4: {
        'title': 'Basic Plot Types with NumPy',
        'description': 'Line plots, scatter plots, bar charts, and histograms',
        'duration': '30-35 minutes',
        'sources': [
            ('video', 16, 30, 'Common plot types with NumPy'),
            ('kopie', 40, 55, 'Scatterplot variations and basic plots')
        ]
    },
    5: {
        'title': 'Plotting with Pandas DataFrames',
        'description': 'Real-world data, DataFrame plotting, and pandas integration',
        'duration': '25-30 minutes',
        'sources': [
            ('video', 33, 66, 'Pandas integration with real datasets')
        ]
    },
    6: {
        'title': 'Subplots and Multi-Panel Figures',
        'description': 'Creating complex layouts with multiple axes',
        'duration': '25-30 minutes',
        'sources': [
            ('kopie', 57, 67, 'Multiple panels and subplots'),
            ('video', 31, 32, 'Subplots examples'),
            ('fundamentals', 24, 26, 'Multiple subplots practical example')
        ]
    },
    7: {
        'title': 'Customization Fundamentals',
        'description': 'Labels, legends, colors, line styles, and axis limits',
        'duration': '30-35 minutes',
        'sources': [
            ('kopie', 89, 96, 'Labels and legends'),
            ('video', 75, 95, 'Customization options'),
            ('kopie', 98, 110, 'Colors and line styles')
        ]
    },
    8: {
        'title': 'Advanced Customization',
        'description': 'Ticks, styles, themes, rcParams, and annotations',
        'duration': '25-30 minutes',
        'sources': [
            ('fundamentals', 13, 23, 'Comprehensive ticks guide'),
            ('kopie', 111, 122, 'Formatting, rcParams, and styles')
        ]
    },
    9: {
        'title': 'Special Plot Types and Scales',
        'description': 'Logarithmic scales, scientific notation, advanced scatter plots',
        'duration': '20-25 minutes',
        'sources': [
            ('kopie', 124, 131, 'Axis appearance, log scale, and advanced features')
        ]
    },
    10: {
        'title': 'Figure Configuration and Export',
        'description': 'Figure size, DPI, saving in multiple formats',
        'duration': '15-20 minutes',
        'sources': [
            ('kopie', 69, 77, 'Figure configuration and saving'),
            ('video', 98, 98, 'Saving plots with figsave()')
        ]
    },
    11: {
        'title': 'Practical Integration & Best Practices',
        'description': 'Complete workflows, combining techniques, common pitfalls',
        'duration': '20-25 minutes',
        'sources': [
            ('fundamentals', 44, 44, 'Practical growth curve example'),
            ('video', 67, 74, 'OO method with pandas - advanced integration')
        ]
    },
    12: {
        'title': 'Self-Assessment & Next Steps',
        'description': 'Quiz questions, challenge exercises, and further resources',
        'duration': '10-15 minutes',
        'sources': [
            ('fundamentals', 45, 45, 'Quiz section')
        ]
    }
}


def read_notebook(filepath: Path) -> nbformat.NotebookNode:
    """
    Read a Jupyter notebook from disk.
    
    Args:
        filepath: Path to the notebook file
        
    Returns:
        NotebookNode object containing the notebook data
        
    Raises:
        FileNotFoundError: If the notebook file doesn't exist
        nbformat.reader.NotJSONError: If the file is not a valid notebook
    """
    logger.info(f"Reading notebook: {filepath}")
    
    if not filepath.exists():
        raise FileNotFoundError(f"Notebook not found: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        cell_count = len(notebook.cells)
        logger.info(f"Successfully read notebook with {cell_count} cells")
        return notebook
        
    except Exception as e:
        logger.error(f"Error reading notebook {filepath}: {e}")
        raise


def extract_cells(
    notebook: nbformat.NotebookNode,
    start_idx: int,
    end_idx: int
) -> List[nbformat.NotebookNode]:
    """
    Extract a range of cells from a notebook.
    
    Args:
        notebook: Source notebook
        start_idx: Starting cell index (0-based)
        end_idx: Ending cell index (inclusive)
        
    Returns:
        List of extracted cells
        
    Note:
        Cell indices are 0-based. If end_idx exceeds the notebook length,
        it will be clamped to the last cell.
    """
    total_cells = len(notebook.cells)
    
    # Clamp indices to valid range
    start_idx = max(0, start_idx)
    end_idx = min(end_idx, total_cells - 1)
    
    if start_idx > end_idx:
        logger.warning(f"Invalid range: start={start_idx}, end={end_idx}")
        return []
    
    extracted = notebook.cells[start_idx:end_idx + 1]
    logger.info(f"Extracted {len(extracted)} cells (indices {start_idx}-{end_idx})")
    
    return extracted


def create_section_header(
    section_num: int,
    title: str,
    description: str,
    duration: str
) -> nbformat.NotebookNode:
    """
    Create a markdown cell for a section header.
    
    Args:
        section_num: Section number
        title: Section title
        description: Brief description of the section
        duration: Estimated time to complete
        
    Returns:
        Markdown cell with formatted section header
    """
    header_text = f"""---

# Section {section_num}: {title}

**Description:** {description}

**Estimated Time:** {duration}

---
"""
    return new_markdown_cell(header_text)


def create_subsection_header(source_name: str, description: str) -> nbformat.NotebookNode:
    """
    Create a markdown cell for a subsection header.
    
    Args:
        source_name: Name of the source notebook
        description: Description of the content
        
    Returns:
        Markdown cell with formatted subsection header
    """
    subsection_text = f"""### From {source_name}
*{description}*
"""
    return new_markdown_cell(subsection_text)


def create_introduction() -> List[nbformat.NotebookNode]:
    """
    Create introduction cells for the combined notebook.
    
    Returns:
        List of cells containing the notebook introduction
    """
    intro_cells = []
    
    # Title cell
    title_md = """# Matplotlib Complete Guide
## A Comprehensive Tutorial from Basics to Advanced

This notebook combines the best elements from three excellent matplotlib resources:
- **Kopie_von_Intro_to_matplotlib.ipynb** - Comprehensive reference material
- **matplotlib_fundamentals_explained.ipynb** - Excellent conceptual explanations
- **introduction-to-matplotlib-video.ipynb** - Practical, hands-on examples

**Total Duration:** Approximately 4-5 hours (with exercises)

**Prerequisites:**
- Basic Python knowledge
- Familiarity with Jupyter notebooks
- NumPy basics (helpful but not required)

**Learning Objectives:**
By the end of this notebook, you will be able to:
1. Understand matplotlib's architecture (Figure, Axes, pyplot vs OO interface)
2. Create various plot types (line, scatter, bar, histogram)
3. Work with both NumPy arrays and Pandas DataFrames
4. Customize plots professionally (colors, styles, labels, legends)
5. Create complex multi-panel figures
6. Export publication-quality figures
7. Apply best practices for data visualization

---
"""
    intro_cells.append(new_markdown_cell(title_md))
    
    # Table of contents
    toc_md = """## Table of Contents

1. **Introduction & Setup** (15-20 min)
2. **Core Concepts - Figure Architecture** (20-25 min)
3. **Understanding Data for Plotting** (15-20 min)
4. **Basic Plot Types with NumPy** (30-35 min)
5. **Plotting with Pandas DataFrames** (25-30 min)
6. **Subplots and Multi-Panel Figures** (25-30 min)
7. **Customization Fundamentals** (30-35 min)
8. **Advanced Customization** (25-30 min)
9. **Special Plot Types and Scales** (20-25 min)
10. **Figure Configuration and Export** (15-20 min)
11. **Practical Integration & Best Practices** (20-25 min)
12. **Self-Assessment & Next Steps** (10-15 min)

---
"""
    intro_cells.append(new_markdown_cell(toc_md))
    
    return intro_cells


def translate_german_cell(cell: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """
    Translate German content in a cell to English.
    
    Note: This is a placeholder for actual translation logic.
    In production, you would use a translation API or manual translation.
    
    Args:
        cell: Cell to translate
        
    Returns:
        Translated cell (currently returns original cell with a note)
    """
    # For now, just add a note that translation is needed
    # In production, implement actual translation logic
    if cell.cell_type == 'markdown':
        # Check if content appears to be in German (simple heuristic)
        german_indicators = ['der', 'die', 'das', 'und', 'ist', 'sind', 'werden']
        content_lower = cell.source.lower()
        
        if any(indicator in content_lower for indicator in german_indicators):
            logger.warning("German content detected - translation needed")
            # Add translation note
            cell.source = f"<!-- Translation needed from German -->\n\n{cell.source}"
    
    return cell


def combine_notebooks(
    sections_to_build: List[int],
    base_dir: Path,
    output_path: Path
) -> None:
    """
    Main function to combine notebooks into a single comprehensive guide.
    
    Args:
        sections_to_build: List of section numbers to include
        base_dir: Base directory containing source notebooks
        output_path: Path where the combined notebook will be saved
    """
    logger.info("=" * 70)
    logger.info("Starting notebook combination process")
    logger.info(f"Building sections: {sections_to_build}")
    logger.info("=" * 70)
    
    # Create new notebook
    combined_nb = new_notebook()
    
    # Add introduction
    logger.info("Adding introduction...")
    combined_nb.cells.extend(create_introduction())
    
    # Load source notebooks (lazy loading - only when needed)
    loaded_notebooks = {}
    
    # Process each section
    for section_num in sorted(sections_to_build):
        if section_num not in SECTIONS:
            logger.warning(f"Section {section_num} not defined, skipping")
            continue
        
        section = SECTIONS[section_num]
        logger.info(f"\n{'=' * 70}")
        logger.info(f"Processing Section {section_num}: {section['title']}")
        logger.info(f"{'=' * 70}")
        
        # Add section header
        header_cell = create_section_header(
            section_num,
            section['title'],
            section['description'],
            section['duration']
        )
        combined_nb.cells.append(header_cell)
        
        # Process each source in the section
        for source_name, start_idx, end_idx, description in section['sources']:
            logger.info(f"\nProcessing source: {source_name} (cells {start_idx}-{end_idx})")
            
            # Load notebook if not already loaded
            if source_name not in loaded_notebooks:
                notebook_path = base_dir / SOURCE_NOTEBOOKS[source_name]
                try:
                    loaded_notebooks[source_name] = read_notebook(notebook_path)
                except Exception as e:
                    logger.error(f"Failed to load {source_name}: {e}")
                    continue
            
            # Extract cells
            source_nb = loaded_notebooks[source_name]
            cells = extract_cells(source_nb, start_idx, end_idx)
            
            if not cells:
                logger.warning(f"No cells extracted from {source_name}")
                continue
            
            # Add subsection header
            subsection_header = create_subsection_header(source_name, description)
            combined_nb.cells.append(subsection_header)
            
            # Translate German content if from fundamentals notebook
            if source_name == 'fundamentals':
                cells = [translate_german_cell(cell) for cell in cells]
            
            # Add extracted cells
            combined_nb.cells.extend(cells)
            logger.info(f"Added {len(cells)} cells from {source_name}")
    
    # Add conclusion
    conclusion_md = """---

## Conclusion

Congratulations! You've completed the Matplotlib Complete Guide.

You now have a solid foundation in:
- Matplotlib's architecture and design philosophy
- Creating and customizing various plot types
- Working with both NumPy and Pandas data
- Professional plot styling and formatting
- Complex multi-panel figures
- Best practices for data visualization

### Next Steps

1. **Practice:** Apply these concepts to your own datasets
2. **Explore:** Check out matplotlib's gallery for inspiration
3. **Advanced Topics:** Consider learning about:
   - 3D plotting with mplot3d
   - Animations with matplotlib.animation
   - Interactive plots with widgets
   - Integration with other libraries (seaborn, plotly)

### Resources

- [Matplotlib Official Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Matplotlib Cheat Sheets](https://matplotlib.org/cheatsheets/)
- [Python Graph Gallery](https://python-graph-gallery.com/)

**Happy Plotting! 📊📈📉**
"""
    combined_nb.cells.append(new_markdown_cell(conclusion_md))
    
    # Save combined notebook
    logger.info(f"\n{'=' * 70}")
    logger.info(f"Saving combined notebook to: {output_path}")
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(combined_nb, f)
        
        total_cells = len(combined_nb.cells)
        logger.info(f"Successfully saved notebook with {total_cells} cells")
        logger.info("=" * 70)
        logger.info("✓ Notebook combination complete!")
        
    except Exception as e:
        logger.error(f"Error saving notebook: {e}")
        raise


def parse_sections_argument(sections_arg: str) -> List[int]:
    """
    Parse the sections command-line argument.
    
    Args:
        sections_arg: String like "1-3", "all", or "1,3,5"
        
    Returns:
        List of section numbers to build
        
    Examples:
        "1-3" -> [1, 2, 3]
        "all" -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        "1,3,5" -> [1, 3, 5]
    """
    if sections_arg.lower() == 'all':
        return list(range(1, 13))
    
    sections = []
    
    # Handle comma-separated values
    parts = sections_arg.split(',')
    
    for part in parts:
        part = part.strip()
        
        # Handle ranges (e.g., "1-3")
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                sections.extend(range(start, end + 1))
            except ValueError:
                logger.error(f"Invalid range format: {part}")
                sys.exit(1)
        else:
            # Handle single numbers
            try:
                sections.append(int(part))
            except ValueError:
                logger.error(f"Invalid section number: {part}")
                sys.exit(1)
    
    # Remove duplicates and sort
    sections = sorted(set(sections))
    
    # Validate section numbers
    invalid = [s for s in sections if s < 1 or s > 12]
    if invalid:
        logger.error(f"Invalid section numbers: {invalid}. Must be between 1 and 12.")
        sys.exit(1)
    
    return sections


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Combine matplotlib notebooks into a comprehensive guide',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sections 1-3          Build sections 1 through 3
  %(prog)s --sections 4-7          Build sections 4 through 7
  %(prog)s --sections all          Build all sections
  %(prog)s --sections 1,3,5        Build sections 1, 3, and 5
  %(prog)s --sections 1-3,7,9-11   Build sections 1-3, 7, and 9-11

Section Overview:
  1.  Introduction & Setup
  2.  Core Concepts - Figure Architecture
  3.  Understanding Data for Plotting
  4.  Basic Plot Types with NumPy
  5.  Plotting with Pandas DataFrames
  6.  Subplots and Multi-Panel Figures
  7.  Customization Fundamentals
  8.  Advanced Customization
  9.  Special Plot Types and Scales
  10. Figure Configuration and Export
  11. Practical Integration & Best Practices
  12. Self-Assessment & Next Steps
        """
    )
    
    parser.add_argument(
        '--sections',
        type=str,
        required=True,
        help='Sections to build (e.g., "1-3", "all", "1,3,5")'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=OUTPUT_NOTEBOOK,
        help=f'Output notebook path (default: {OUTPUT_NOTEBOOK})'
    )
    
    parser.add_argument(
        '--base-dir',
        type=str,
        default='.',
        help='Base directory containing source notebooks (default: current directory)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Parse sections argument
    sections = parse_sections_argument(args.sections)
    
    # Convert paths
    base_dir = Path(args.base_dir).resolve()
    output_path = base_dir / args.output
    
    # Verify base directory exists
    if not base_dir.exists():
        logger.error(f"Base directory does not exist: {base_dir}")
        sys.exit(1)
    
    # Verify source notebooks exist
    missing = []
    for name, filename in SOURCE_NOTEBOOKS.items():
        if not (base_dir / filename).exists():
            missing.append(filename)
    
    if missing:
        logger.error(f"Missing source notebooks: {', '.join(missing)}")
        logger.error(f"Please ensure all source notebooks are in: {base_dir}")
        sys.exit(1)
    
    # Run combination
    try:
        combine_notebooks(sections, base_dir, output_path)
        logger.info(f"\n✓ Success! Combined notebook saved to: {output_path}")
        
    except KeyboardInterrupt:
        logger.warning("\n\nProcess interrupted by user")
        sys.exit(1)
        
    except Exception as e:
        logger.error(f"\n✗ Error: {e}", exc_info=args.verbose)
        sys.exit(1)


if __name__ == '__main__':
    main()

# Made with Bob
