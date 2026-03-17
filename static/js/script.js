document.addEventListener('DOMContentLoaded', () => {
    
    // Theme Toggling Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const body = document.getElementById('body');

    // Check local storage for theme preference
    const currentTheme = localStorage.getItem('theme');
    
    // Function to set theme
    const setTheme = (isDark) => {
        if (isDark) {
            body.classList.add('dark-mode');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-mode');
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
            localStorage.setItem('theme', 'light');
        }
    };

    // Initialize theme
    // Default to dark mode if no preference since it fits anime themes well
    if (currentTheme === 'light') {
        setTheme(false);
    } else {
        setTheme(true);
    }

    // Toggle click handler
    themeToggleBtn.addEventListener('click', () => {
        const isDark = !body.classList.contains('dark-mode');
        setTheme(isDark);
    });

    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.opacity = '0';
                setTimeout(() => {
                    msg.style.display = 'none';
                }, 300); // Wait for transition fade if we had one
            });
        }, 5000);
    }
});
