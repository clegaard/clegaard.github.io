# Copilot Instructions for Hugo Gallery Site

## Project Overview
This is a personal photography portfolio built with Hugo and the `hugo-theme-gallery` theme. The site features a landing page that directs visitors to either the photography gallery or personal blog sections, each with distinct content organization patterns.

## Architecture & Content Organization

### Content Structure Pattern
```
content/
├── _index.md              # Landing page with gallery/blog navigation
├── gallery/               # Photography section
│   ├── _index.md         # Gallery homepage
│   ├── animals/          # Branch bundle (has _index.md + subfolders)
│   │   ├── _index.md     # Category landing page
│   │   ├── amphibians/   # Leaf bundle (has index.md + images)
│   │   │   ├── index.md  # Gallery page
│   │   │   └── *.jpg     # Gallery images
│   │   └── birds/
│   └── private/          # Private gallery (params.private: true)
└── blog/                 # Blog section
    ├── _index.md         # Blog homepage
    └── welcome/          # Blog post (leaf bundle)
        └── index.md      # Blog post content
```

**Critical Patterns**: 
- **Landing page** (`content/_index.md`) = main entry point with navigation to gallery/blog
- **Gallery section** (`content/gallery/`) = contains all photo albums and collections
- **Blog section** (`content/blog/`) = contains blog posts and articles
- **Branch bundles** (`_index.md`) = category/section pages that list sub-content
- **Leaf bundles** (`index.md`) = actual galleries or blog posts with content
- Only bundles with images are displayed in gallery sections

### Front Matter Conventions
```yaml
# Essential front matter for galleries
title: "Gallery Name"
date: 2023-01-12          # Used for sorting (newest first)
resources:
  - src: cover-image.jpg
    params:
      cover: true         # Designates album thumbnail
params:
  private: true          # Hides from listings/RSS (access by direct link)
  featured: true         # Shows on homepage even if private
```

## Development Workflows

### Local Development
```bash
# Start development server
npm run dev
# OR
hugo server

# Build for production
npm run build
# OR
hugo --gc --minify
```

### Image Management
- **Image Format**: Use JPEG/PNG only - **avoid WebP** (Hugo WebP bug causes dull images)
- **Album Cover**: First image with `*feature*` in filename, or use `resources.params.cover: true`
- **Image Quality**: Set to 100% in `hugo.toml` (`imaging.quality = 100`)
- Use `move_images.sh` for bulk image operations from external directories

### Git Submodule (Theme)
```bash
# Initialize theme submodule
git submodule update --init --recursive

# Update theme
cd themes/gallery && git pull origin main
```

## Key Configuration Files

### `hugo.toml` Critical Settings
- `theme = "gallery"` - Points to git submodule
- `baseURL` - Must match GitHub Pages URL for proper deployment
- `defaultTheme = "dark"` - Site-wide theme preference
- `imaging.quality = 100` - Prevent image degradation
- `timeout = "120s"` - Extended timeout for large image processing

### GitHub Actions Deployment
- Deploys from `hugo` branch to GitHub Pages
- Uses Hugo Extended v0.147.1
- Requires `submodules: recursive` checkout for theme
- Caches Hugo build for performance

## Content Creation Patterns

### New Gallery Album
1. Create folder in `content/gallery/` with descriptive name
2. Add `index.md` with proper front matter
3. Place images in same folder
4. Designate cover image via filename (`*feature*`) or front matter

### New Blog Post
1. Create folder in `content/blog/post-name/` 
2. Add `index.md` with front matter including `title`, `date`, `description`
3. Write content in Markdown format
4. Posts automatically appear in blog listing

### New Gallery Category
1. Create `content/gallery/category-name/_index.md` (branch bundle)
2. Add cover image and set `resources.params.cover: true`
3. Create sub-galleries as leaf bundles within category

### Private Albums
- Set `params.private: true` in front matter
- Albums remain accessible via direct URL but hidden from listings
- Use `params.featured: true` to show private albums on homepage

### Menu Navigation
Add to `hugo.toml` or front matter:
```yaml
menus: "main"
# OR
menus:
  main:
    name: "Custom Name"
    weight: 1
```

## Custom Layouts

### Landing Page
- Uses `layouts/_default/home.html` for main entry point
- Features dual-path navigation to gallery and blog
- Includes custom CSS for landing page styling

### Gallery Section
- Uses `layouts/gallery/list.html` for gallery homepage
- Inherits album display functionality from theme
- Shows featured albums and category navigation

### Blog Section  
- Uses `layouts/blog/list.html` for blog homepage
- Uses `layouts/blog/single.html` for individual posts
- Includes post metadata, navigation, and styling

## Common Tasks

### Adding New Category
1. Create `content/gallery/category-name/_index.md` (branch bundle)
2. Add cover image and set `resources.params.cover: true`
3. Create sub-galleries as leaf bundles within category

### Bulk Image Import
1. Use `move_images.sh` script for moving images from external directory
2. Organize into appropriate `content/gallery/` structure
3. Update front matter for each gallery

### Theme Customization
- Custom CSS: `assets/css/custom.css`
- HTML overrides: `layouts/partials/head-custom.html`
- Theme files located in `themes/gallery/` (git submodule)
- Landing page layout: `layouts/_default/home.html`
- Blog layouts: `layouts/blog/list.html` and `layouts/blog/single.html`
- Gallery layout: `layouts/gallery/list.html`