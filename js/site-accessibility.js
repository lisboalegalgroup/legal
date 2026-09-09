(function () {
    'use strict';

    function syncMobileMenu() {
        const toggle = document.getElementById('mobile-menu');
        const nav = document.getElementById('primary-navigation') || document.querySelector('.nav-links');
        if (!toggle || !nav) return;

        toggle.setAttribute('aria-expanded', nav.classList.contains('active') ? 'true' : 'false');

        nav.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                nav.classList.remove('active');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });

        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && nav.classList.contains('active')) {
                nav.classList.remove('active');
                toggle.setAttribute('aria-expanded', 'false');
                toggle.focus();
            }
        });

        toggle.addEventListener('click', function () {
            window.setTimeout(function () {
                toggle.setAttribute('aria-expanded', nav.classList.contains('active') ? 'true' : 'false');
            }, 0);
        });
    }

    function enableKeyboardControls() {
        document.querySelectorAll('[onclick]').forEach(function (element) {
            if (/^(BUTTON|A|INPUT|SELECT|TEXTAREA)$/.test(element.tagName)) return;
            if (!element.hasAttribute('role')) element.setAttribute('role', 'button');
            if (!element.hasAttribute('tabindex')) element.setAttribute('tabindex', '0');
            element.addEventListener('keydown', function (event) {
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    element.click();
                }
            });
        });
    }

    function improveDynamicRegions() {
        document.querySelectorAll('[id^="rp-"], [id^="resultado"], .result, .resultado').forEach(function (region) {
            if (!region.hasAttribute('role')) region.setAttribute('role', 'status');
            if (!region.hasAttribute('aria-live')) region.setAttribute('aria-live', 'polite');
            region.setAttribute('aria-atomic', 'true');
        });
    }

    document.addEventListener('DOMContentLoaded', function () {
        syncMobileMenu();
        enableKeyboardControls();
        improveDynamicRegions();
    });
}());
