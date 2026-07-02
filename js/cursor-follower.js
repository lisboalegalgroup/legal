/**
 * Cursor Follower - Lisboa Legal Group / San Andrés Legal Group
 * Creates a smooth, elegant blue dot trailing effect following the mouse pointer.
 */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Feature detection: only enable on devices with hover capabilities (desktops/laptops with mouse)
    if (window.matchMedia('(hover: none)').matches || window.matchMedia('(pointer: coarse)').matches) {
        return;
    }

    // 2. Create cursor element (only the dot, no outer halo)
    const dot = document.createElement('div');
    dot.className = 'custom-cursor-dot';
    document.body.appendChild(dot);

    // 3. Coordinate tracking variables
    let mouseX = -100;
    let mouseY = -100;
    
    let dotX = -100;
    let dotY = -100;
    
    let isVisible = false;
    let hasMoved = false;

    // Smoothness interpolation factor (lower = smoother/slower)
    const LERP_DOT = 0.22;

    // 4. Event listeners
    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Position instantly on the first movement to avoid sliding in from (-100, -100)
        if (!hasMoved) {
            dotX = mouseX;
            dotY = mouseY;
            hasMoved = true;
        }

        if (!isVisible) {
            dot.classList.add('visible');
            isVisible = true;
        }
    });

    // Hide cursor element when leaving the document viewport
    document.addEventListener('mouseleave', () => {
        dot.classList.remove('visible');
        isVisible = false;
    });

    document.addEventListener('mouseenter', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        dot.classList.add('visible');
        isVisible = true;
    });

    // 5. Animation loop (using requestAnimationFrame for 60fps+ performance)
    function updatePositions() {
        if (hasMoved) {
            // Linear interpolation (lerp) formulas: Current + (Target - Current) * Factor
            dotX += (mouseX - dotX) * LERP_DOT;
            dotY += (mouseY - dotY) * LERP_DOT;
            
            // Apply transform (more performant than updating top/left directly)
            dot.style.transform = `translate3d(calc(${dotX}px - 50%), calc(${dotY}px - 50%), 0)`;
        }
        
        requestAnimationFrame(updatePositions);
    }
    
    requestAnimationFrame(updatePositions);

    // 6. Interactive elements hover state
    const clickablesSelector = 'a, button, .btn, [role="button"], input[type="submit"], input[type="button"], select, .card-clickable, .service-card, .profile-social-icons a';
    
    document.addEventListener('mouseover', (e) => {
        if (e.target.closest(clickablesSelector)) {
            dot.classList.add('hovering');
        }
    });

    document.addEventListener('mouseout', (e) => {
        if (e.target.closest(clickablesSelector)) {
            // Check if we didn't immediately move to another clickable element
            if (!e.relatedTarget || !e.relatedTarget.closest(clickablesSelector)) {
                dot.classList.remove('hovering');
            }
        }
    });
});
