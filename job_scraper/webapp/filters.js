/**
 * Modular Keyword Filter Module
 * Provides centralized filter management for all tabs
 */

// Filter state
let includeKeywords = [];
let excludeKeywords = [
    { keyword: 'Senior', matchType: 'whole' },
    { keyword: 'manager', matchType: 'partial' },
    { keyword: 'Manager', matchType: 'whole' }
];

/**
 * Initialize filters from localStorage
 */
function initializeFilters() {
    const savedInclude = localStorage.getItem('includeKeywords');
    const savedExclude = localStorage.getItem('excludeKeywords');
    
    if (savedInclude) {
        try {
            includeKeywords = JSON.parse(savedInclude);
        } catch (e) {
            console.error('Error loading include keywords:', e);
        }
    }
    
    if (savedExclude) {
        try {
            excludeKeywords = JSON.parse(savedExclude);
        } catch (e) {
            console.error('Error loading exclude keywords:', e);
        }
    }
}

/**
 * Save filters to localStorage
 */
function saveFilters() {
    localStorage.setItem('includeKeywords', JSON.stringify(includeKeywords));
    localStorage.setItem('excludeKeywords', JSON.stringify(excludeKeywords));
}

/**
 * Get current filter state for API calls
 */
function getFilterPayload() {
    return {
        includeKeywords: includeKeywords,
        excludeKeywords: excludeKeywords
    };
}

/**
 * Add include keyword
 */
function addIncludeKeyword() {
    const input = document.getElementById('newIncludeKeyword');
    const matchTypeSelect = document.getElementById('includeKeywordMatchType');
    const keyword = input.value.trim();
    const matchType = matchTypeSelect.value;
    
    if (keyword && !includeKeywords.some(k => k.keyword === keyword)) {
        includeKeywords.push({ keyword, matchType });
        input.value = '';
        saveFilters();
        renderIncludeKeywords();
        notifyFilterChange();
    }
}

/**
 * Add suggested include keyword
 */
function addSuggestedIncludeKeyword(keyword) {
    if (!includeKeywords.some(k => k.keyword === keyword)) {
        includeKeywords.push({ keyword, matchType: 'whole' });
        saveFilters();
        renderIncludeKeywords();
        notifyFilterChange();
    }
}

/**
 * Remove include keyword
 */
function removeIncludeKeyword(index) {
    includeKeywords.splice(index, 1);
    saveFilters();
    renderIncludeKeywords();
    notifyFilterChange();
}

/**
 * Add exclude keyword
 */
function addExcludeKeyword() {
    const input = document.getElementById('newExcludeKeyword');
    const matchTypeSelect = document.getElementById('excludeKeywordMatchType');
    const keyword = input.value.trim();
    const matchType = matchTypeSelect.value;
    
    if (keyword && !excludeKeywords.some(k => k.keyword === keyword)) {
        excludeKeywords.push({ keyword, matchType });
        input.value = '';
        saveFilters();
        renderExcludeKeywords();
        notifyFilterChange();
    }
}

/**
 * Remove exclude keyword
 */
function removeExcludeKeyword(index) {
    excludeKeywords.splice(index, 1);
    saveFilters();
    renderExcludeKeywords();
    notifyFilterChange();
}

/**
 * Render include keywords UI
 */
function renderIncludeKeywords() {
    const container = document.getElementById('includeKeywordsList');
    if (!container) return;
    
    container.innerHTML = includeKeywords.map((kw, index) => `
        <span class="keyword-tag include-keyword ${kw.matchType === 'whole' ? 'whole-word' : ''}">
            ${kw.keyword}
            <span class="keyword-match-type">(${kw.matchType === 'whole' ? 'Ganzes Wort' : 'Teil'})</span>
            <button onclick="removeIncludeKeyword(${index})" class="keyword-remove">×</button>
        </span>
    `).join('');
}

/**
 * Render exclude keywords UI
 */
function renderExcludeKeywords() {
    const container = document.getElementById('excludeKeywordsList');
    if (!container) return;
    
    container.innerHTML = excludeKeywords.map((kw, index) => `
        <span class="keyword-tag ${kw.matchType === 'whole' ? 'whole-word' : ''}">
            ${kw.keyword}
            <span class="keyword-match-type">(${kw.matchType === 'whole' ? 'Ganzes Wort' : 'Teil'})</span>
            <button onclick="removeExcludeKeyword(${index})" class="keyword-remove">×</button>
        </span>
    `).join('');
}

/**
 * Notify all tabs that filters have changed
 * This function should be called whenever filters are modified
 */
function notifyFilterChange() {
    // Dispatch custom event that tabs can listen to
    window.dispatchEvent(new CustomEvent('filtersChanged', {
        detail: getFilterPayload()
    }));
}

/**
 * Check if any filters are active
 */
function hasActiveFilters() {
    return includeKeywords.length > 0 || excludeKeywords.length > 0;
}

/**
 * Clear all filters
 */
function clearAllFilters() {
    includeKeywords = [];
    excludeKeywords = [];
    saveFilters();
    renderIncludeKeywords();
    renderExcludeKeywords();
    notifyFilterChange();
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    initializeFilters();
    renderIncludeKeywords();
    renderExcludeKeywords();
});

// Made with Bob
