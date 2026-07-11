def load_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

/* Main resets */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0b0f19;
    color: #f3f4f6;
}

.stApp {
    background-color: #0b0f19;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
    margin-bottom: 30px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.logo-container {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 24px;
    color: #ffffff;
}

.logo-icon {
    background-color: #3b82f6;
    color: white;
    padding: 4px 8px;
    border-radius: 6px;
    font-size: 16px;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 20px;
}

.nav-link {
    color: #9ca3af;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: 0.2s;
}

.nav-link:hover {
    color: #ffffff;
}

/* Pill Tag */
.pill-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background-color: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 6px 12px;
    border-radius: 50px;
    font-size: 13px;
    color: #9ca3af;
    font-weight: 500;
    margin-bottom: 20px;
}

.pill-dot {
    width: 6px;
    height: 6px;
    background-color: #10b981;
    border-radius: 50%;
}

/* Hero Content */
.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 48px;
    font-weight: 800;
    line-height: 1.15;
    color: #ffffff;
    margin-bottom: 20px;
}

.hero-highlight {
    color: #60a5fa; /* light blue */
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.6;
    color: #9ca3af;
    margin-bottom: 40px;
}

/* Stats Row */
.stats-container {
    display: flex;
    gap: 30px;
    margin-top: 30px;
}

.stat-item {
    flex: 1;
}

.stat-number {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
}

.stat-label {
    font-size: 13px;
    color: #6b7280;
    margin-top: 4px;
    line-height: 1.4;
}

/* Card Container (Right Side Panel) */
.input-card {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 24px;
    color: #111827;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.3);
}

.card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 15px;
}

.card-footer-text {
    font-size: 12px;
    color: #6b7280;
    text-align: center;
    margin-top: 12px;
}

/* White Section Transition */
.white-section {
    background-color: #ffffff;
    color: #111827;
    padding: 60px 0;
    margin-top: 40px;
    border-radius: 24px 24px 0 0;
    box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.05);
}

.brand-bar-title {
    font-size: 12px;
    font-weight: 700;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-align: center;
    margin-bottom: 25px;
}

.brand-links {
    display: flex;
    justify-content: center;
    gap: 40px;
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 16px;
    color: #d1d5db;
    margin-bottom: 60px;
}

.brand-link-item {
    transition: 0.2s;
}
.brand-link-item:hover {
    color: #4b5563;
}

/* Process Section */
.process-pre {
    font-size: 12px;
    font-weight: 700;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-align: center;
    margin-bottom: 10px;
}

.process-title {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #111827;
    text-align: center;
    margin-bottom: 12px;
}

.process-subtitle {
    font-size: 15px;
    color: #4b5563;
    text-align: center;
    max-width: 600px;
    margin: 0 auto 50px auto;
    line-height: 1.6;
}

.process-card {
    background-color: #f9fafb;
    border: 1px solid #f3f4f6;
    border-radius: 12px;
    padding: 24px;
    height: 100%;
}

.process-card-icon {
    background-color: #eff6ff;
    color: #2563eb;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-bottom: 16px;
}

.process-card-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 16px;
    color: #111827;
    margin-bottom: 8px;
}

.process-card-desc {
    font-size: 14px;
    color: #4b5563;
    line-height: 1.5;
}

/* Footer Section */
.footer-bar {
    background-color: #0b0f19;
    color: #6b7280;
    padding: 30px 0;
    font-size: 13px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Dashboard styles (retained/cleaned) */
.dashboard-card {
    background: #1e293b;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,.25);
    height: 320px;
}

.score-circle {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.score-inner {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: #1e293b;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.score-number {
    font-size: 45px;
    font-weight: bold;
    color: white;
}

.score-text {
    font-size: 18px;
    color: #9ca3af;
}

.glass {
    background: rgba(30,41,59,.95);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,.35);
    margin-bottom: 25px;
}

.skill-badge {
    display: inline-block;
    background: #064e3b;
    color: #4ade80;
    padding: 10px 18px;
    border-radius: 50px;
    margin: 8px;
    font-size: 15px;
    font-weight: 600;
}

.missing-badge {
    display: inline-block;
    background: #7c2d12;
    color: #fdba74;
    padding: 10px 18px;
    border-radius: 50px;
    margin: 8px;
    font-size: 15px;
    font-weight: 600;
}

.tip {
    background: #111827;
    border-left: 5px solid #4f46e5;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
}

.title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 20px;
}
</style>
"""