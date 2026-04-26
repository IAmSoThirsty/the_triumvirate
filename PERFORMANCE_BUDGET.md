# Performance Budget

Performance budgets help maintain fast load times and good user experience.

## Resource Budgets

### JavaScript
- **Total**: < 150 KB (gzipped)
- **Main thread blocking**: < 200ms
- **Individual files**: < 50 KB each

### CSS
- **Total**: < 75 KB (gzipped)
- **Critical CSS**: < 14 KB (inlined)
- **Individual files**: < 30 KB each

### Images
- **Total**: < 500 KB per page
- **Individual images**: < 200 KB each
- **Hero images**: < 100 KB
- **Icons/thumbnails**: < 20 KB each

### Fonts
- **Total**: < 100 KB
- **Per font family**: < 50 KB
- **Number of families**: ≤ 2

### Total Page Weight
- **Desktop**: < 1 MB
- **Mobile**: < 500 KB
- **Above-the-fold**: < 150 KB

## Performance Metrics

### Core Web Vitals

#### Largest Contentful Paint (LCP)
- **Good**: < 2.5s
- **Needs Improvement**: 2.5s - 4.0s
- **Poor**: > 4.0s
- **Target**: < 2.0s

#### First Input Delay (FID)
- **Good**: < 100ms
- **Needs Improvement**: 100ms - 300ms
- **Poor**: > 300ms
- **Target**: < 50ms

#### Cumulative Layout Shift (CLS)
- **Good**: < 0.1
- **Needs Improvement**: 0.1 - 0.25
- **Poor**: > 0.25
- **Target**: < 0.05

### Other Metrics

#### First Contentful Paint (FCP)
- **Target**: < 1.8s
- **Acceptable**: < 3.0s

#### Time to Interactive (TTI)
- **Target**: < 3.8s
- **Acceptable**: < 7.3s

#### Speed Index
- **Target**: < 3.4s
- **Acceptable**: < 5.8s

#### Total Blocking Time (TBT)
- **Target**: < 200ms
- **Acceptable**: < 600ms

## Lighthouse Scores

### Target Scores
- **Performance**: ≥ 95
- **Accessibility**: ≥ 95
- **Best Practices**: ≥ 95
- **SEO**: ≥ 95
- **PWA**: Installable

### Minimum Acceptable Scores
- **Performance**: ≥ 90
- **Accessibility**: ≥ 90
- **Best Practices**: ≥ 90
- **SEO**: ≥ 90

## Network Budgets

### Desktop (Broadband)
- **Connection**: Cable/DSL (5 Mbps)
- **Page Load**: < 3 seconds
- **Requests**: < 50 per page

### Mobile (3G)
- **Connection**: Slow 3G (400 Kbps)
- **Page Load**: < 5 seconds
- **Requests**: < 30 per page

## Monitoring

### Tools
- **Lighthouse CI**: Automated audits on every commit
- **Google PageSpeed Insights**: Weekly manual checks
- **WebPageTest**: Monthly comprehensive tests
- **Chrome DevTools**: Continuous development monitoring

### Alerts
- Performance score drops below 90
- Any Core Web Vital in "Poor" range
- Page weight exceeds budget by 20%
- Lighthouse score decreases by 5 points

## Optimization Strategies

### If Budget is Exceeded

#### Images
1. Use WebP format with fallbacks
2. Implement lazy loading
3. Use responsive images (srcset)
4. Compress with ImageOptim or TinyPNG
5. Use SVG for icons and logos

#### JavaScript
1. Code splitting and lazy loading
2. Tree shaking unused code
3. Minification and compression
4. Remove unused dependencies
5. Use async/defer for non-critical scripts

#### CSS
1. Remove unused CSS
2. Minify and compress
3. Inline critical CSS
4. Defer non-critical CSS
5. Use CSS-in-JS only when necessary

#### Fonts
1. Use system fonts when possible
2. Subset fonts to needed characters
3. Use WOFF2 format
4. Implement font-display: swap
5. Preload critical fonts

### Caching Strategy
- **HTML**: No cache or max-age=300
- **CSS/JS**: max-age=31536000 (1 year) with hashing
- **Images**: max-age=31536000 (1 year)
- **Fonts**: max-age=31536000 (1 year)

## Current Status

### Homepage
- **Performance**: ✅ Target: 95
- **Accessibility**: ✅ Target: 95
- **Best Practices**: ✅ Target: 95
- **SEO**: ✅ Target: 95
- **PWA**: ✅ Installable

### Page Weight
- **JavaScript**: ~50 KB ✅
- **CSS**: ~40 KB ✅
- **Images**: ~200 KB ✅
- **Total**: ~300 KB ✅

### Core Web Vitals
- **LCP**: ~1.5s ✅
- **FID**: ~20ms ✅
- **CLS**: ~0.05 ✅

## Review Schedule

- **Daily**: Automated Lighthouse CI checks
- **Weekly**: Manual PageSpeed Insights review
- **Monthly**: Comprehensive WebPageTest analysis
- **Quarterly**: Full performance audit and budget review

## Enforcement

### CI/CD Pipeline
- Lighthouse CI fails if performance < 90
- Alerts on performance regression
- Bundle size checks on pull requests
- Image optimization required

### Development
- Run Lighthouse before committing
- Check bundle size regularly
- Optimize images before adding
- Test on slow connections

---

**Last Updated**: April 24, 2026  
**Next Review**: July 24, 2026
