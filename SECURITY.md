# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The Triumvirate project takes security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Create a Public Issue

Please **do not** open a public GitHub issue for security vulnerabilities. Public disclosure could put users at risk.

### 2. Report Privately

Send an email to: **security@thirstysprojects.com**

Include the following information:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)
- Your contact information

### 3. Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: 1-7 days
  - High: 7-14 days
  - Medium: 14-30 days
  - Low: 30-90 days

### 4. Disclosure Policy

- We will acknowledge receipt of your report
- We will investigate and validate the issue
- We will develop and test a fix
- We will release a security patch
- We will publicly disclose after the fix is deployed
- We will credit the reporter (unless they prefer anonymity)

## Security Best Practices

### For Users

1. **Keep Dependencies Updated**
   ```bash
   npm audit
   npm audit fix
   ```

2. **Use HTTPS**
   - Always access the site via HTTPS
   - Enable HSTS if using a custom domain

3. **Content Security Policy**
   - Our CSP is configured to prevent XSS attacks
   - Report violations to security@thirstysprojects.com

4. **Privacy**
   - We collect minimal analytics data
   - No personal information is stored
   - See our Privacy Policy for details

### For Contributors

1. **Code Review**
   - All code must be reviewed before merging
   - Security-sensitive code requires two approvals

2. **Dependencies**
   - Audit dependencies before adding them
   - Use exact versions in package.json
   - Regularly update and audit dependencies

3. **Sensitive Data**
   - Never commit API keys, tokens, or secrets
   - Use environment variables for sensitive config
   - Review commits before pushing

4. **Testing**
   - Write tests for security-critical code
   - Include security test cases
   - Run full test suite before deployment

## Security Features

### Implemented

✅ **Content Security Policy (CSP)**
- Prevents XSS attacks
- Restricts script sources
- Controls resource loading

✅ **Security Headers**
- X-Frame-Options: Prevents clickjacking
- X-Content-Type-Options: Prevents MIME sniffing
- X-XSS-Protection: Additional XSS protection
- Referrer-Policy: Controls referrer information
- Permissions-Policy: Limits browser features

✅ **HTTPS**
- GitHub Pages provides HTTPS by default
- All resources loaded over HTTPS

✅ **Subresource Integrity (SRI)**
- External resources verified with SRI hashes
- Prevents CDN compromise attacks

✅ **Input Validation**
- All user inputs are validated
- Output encoding prevents injection

✅ **Dependency Security**
- Regular security audits
- Automated vulnerability scanning
- Minimal dependencies

### Planned

⏳ **Rate Limiting**
- API rate limiting (if backend added)
- Form submission throttling

⏳ **Advanced Monitoring**
- Security event logging
- Anomaly detection
- Automated alerts

## Common Vulnerabilities

### We Protect Against

- **Cross-Site Scripting (XSS)**: CSP, output encoding
- **Clickjacking**: X-Frame-Options header
- **MIME Sniffing**: X-Content-Type-Options header
- **Man-in-the-Middle**: HTTPS, HSTS (with custom domain)
- **Dependency Vulnerabilities**: Regular audits
- **Information Disclosure**: Security headers, no verbose errors

### Not Applicable

- **SQL Injection**: No database
- **CSRF**: No state-changing operations
- **Authentication Bypass**: No authentication
- **Session Hijacking**: No sessions

## Compliance

This project follows:
- OWASP Top 10 security guidelines
- GitHub security best practices
- Modern web security standards
- GDPR privacy principles (minimal data collection)

## Security Contacts

- **Security Email**: security@thirstysprojects.com
- **General Contact**: thirstysprojects.com
- **GitHub Issues**: For non-security bugs only

## Acknowledgments

We thank the following security researchers for responsibly disclosing vulnerabilities:

*(List will be updated as vulnerabilities are reported and fixed)*

## Version History

### Version 1.0.0 (April 24, 2026)
- Initial security policy
- Security headers implemented
- CSP configured
- Dependency auditing enabled

---

**Last Updated**: April 24, 2026  
**Policy Version**: 1.0.0
