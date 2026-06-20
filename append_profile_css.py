import os

css_content = """
/* ==========================================================================
   PROFILE PAGE (PBPLAW STYLE)
   ========================================================================== */

/* Breadcrumbs */
.profile-breadcrumb {
    padding: 20px 0;
    margin-top: 80px; /* Offset for fixed header */
    color: var(--text-dark);
    font-size: 0.9rem;
    font-weight: 500;
}
.profile-breadcrumb a {
    color: var(--primary-blue);
    text-decoration: none;
    transition: color 0.3s;
}
.profile-breadcrumb a:hover {
    color: var(--accent-gold);
}
.profile-breadcrumb span {
    margin: 0 10px;
    color: #ccc;
}

/* Profile Hero */
.profile-hero-section {
    padding: 0 0 50px 0;
    background-color: var(--bg-light);
}
.profile-hero-flex {
    display: flex;
    gap: 50px;
    align-items: flex-start;
}
.profile-hero-left {
    flex: 0 0 350px;
}
.profile-hero-left img {
    width: 100%;
    height: auto;
    object-fit: cover;
    object-position: top;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.profile-hero-right {
    flex: 1;
    padding-top: 20px;
}
.profile-name {
    font-size: 4rem;
    color: var(--primary-blue);
    font-family: 'Golos Text', sans-serif;
    line-height: 1.1;
    margin-bottom: 5px;
}
.profile-lastname {
    font-size: 4rem;
    color: var(--primary-blue);
    font-family: 'Golos Text', sans-serif;
    line-height: 1.1;
    font-weight: 800;
    margin-bottom: 15px;
}
.profile-role {
    font-size: 1.2rem;
    color: var(--accent-gold);
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 20px;
}
.profile-desc {
    font-size: 1.1rem;
    color: var(--text-dark);
    margin-bottom: 30px;
    line-height: 1.6;
}

/* Social/Contact Icons */
.profile-social-icons {
    display: flex;
    gap: 15px;
}
.profile-social-icons a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background-color: var(--primary-blue);
    color: var(--white);
    font-size: 1.2rem;
    text-decoration: none;
    transition: all 0.3s ease;
}
.profile-social-icons a:hover {
    background-color: var(--accent-gold);
    transform: translateY(-3px);
}

/* Tabs Section */
.profile-tabs-section {
    padding: 60px 0;
    background-color: var(--white);
}
.profile-tabs-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 40px;
    border-bottom: 2px solid #eee;
    padding-bottom: 15px;
}
.profile-tab-btn {
    background: none;
    border: none;
    padding: 10px 20px;
    font-size: 1.1rem;
    font-family: 'Golos Text', sans-serif;
    font-weight: 600;
    color: #666;
    cursor: pointer;
    transition: all 0.3s;
    border-radius: 5px;
}
.profile-tab-btn:hover {
    color: var(--primary-blue);
    background-color: #f5f5f5;
}
.profile-tab-btn.active {
    color: var(--white);
    background-color: var(--primary-blue);
}
.profile-tab-pane {
    display: none;
    animation: fadeIn 0.5s ease;
}
.profile-tab-pane.active {
    display: block;
}
.profile-tab-content-text {
    font-size: 1.05rem;
    line-height: 1.8;
    color: var(--text-dark);
    max-width: 800px;
}
.profile-tab-content-text p {
    margin-bottom: 20px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 992px) {
    .profile-hero-flex {
        flex-direction: column;
    }
    .profile-hero-left {
        flex: 0 0 auto;
        width: 100%;
        max-width: 400px;
        margin: 0 auto;
    }
    .profile-name, .profile-lastname {
        font-size: 3rem;
    }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("CSS appended to style.css")
