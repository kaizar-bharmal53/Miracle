# Miracle Global School Website

A complete front-end replica of **[miracleducare.com](https://miracleducare.com/)** (Miracle Global School, Upleta).

---

## 📁 Project Structure

```text
Miracle/
├── index.html                  # Main homepage (Hero, About summary, Admission, Why Us, Contact)
├── about.html                  # Full About Us page
├── about/
│   └── index.html              # Clean-URL compatibility for /about/
├── _redirects                  # Netlify redirect rule (/about -> /about.html)
├── robots.txt                  # Robots exclusion standard file
├── server.py                   # Lightweight local development server
├── certificates/
│   └── Building Safety Certificate.pdf # Official safety certificate document
├── css/
│   ├── bootstrap.css           # Bootstrap 4 styling
│   ├── style.css               # Main custom styles and theme
│   ├── responsive.css          # Mobile and responsive layout rules
│   ├── css-circular-prog-bar.css # Progress bar style dependency
│   └── font-awesome.min.css    # FontAwesome 4.3.0 local backup
├── js/
│   ├── jquery-3.4.1.min.js     # jQuery library
│   └── bootstrap.js            # Bootstrap UI interactive behaviors
├── images/
│   ├── hero.png                # Hero illustration
│   ├── hero-bg.png             # Hero background element
│   ├── about.png               # About section illustration
│   ├── admission.png           # Admission section illustration
│   ├── why.png                 # Why Us section illustration
│   ├── menu.png                # Mobile navigation toggle icon
│   ├── favicon.ico             # School favicon
│   ├── prev.png / next.png     # Carousel arrows
│   └── search-icon.png         # Navigation search button placeholder
└── fonts/
    └── fontawesome-webfont.*   # Offline FontAwesome webfont files
```

---

## 🚀 How to Run Locally

### Option 1: Python Built-in Server (Recommended)
Run the included Python server to preview with clean URLs (`/about`):
```bash
python3 server.py
```
Then open: **[http://localhost:8000](http://localhost:8000)**

### Option 2: Direct File Open
You can also directly double-click `index.html` in Finder to open it in any web browser.

---

## 🌐 Deployment

- **Netlify**: Drag & drop this folder into Netlify Drop or connect via Git. The included `_redirects` file will automatically handle routing `/about` to `/about.html`.
- **Vercel / GitHub Pages**: Deploy as a static site. Both `about.html` and `about/index.html` are included to ensure clean routing on any provider.
