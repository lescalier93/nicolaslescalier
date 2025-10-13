# GitHub Deployment Instructions

This guide explains how to deploy your updated Jekyll site to GitHub Pages using the `nicolaslescalier` repository.  Follow these steps after editing your site locally or updating files in this repository.

## 1 – Clone the Repository (Optional)

If you prefer to work locally with Git, clone your repository:

```bash
git clone https://github.com/lescalier93/nicolaslescalier.git
cd nicolaslescalier
```

Create a new branch (optional) to stage changes:

```bash
git checkout -b seo-update-us
```

## 2 – Add or Modify Files

* Copy the contents of the `us_site` directory into the repository root, preserving folder structure (`_includes`, `_layouts`, `services`, etc.).
* Add new pages such as `services/us-mca-expert.md`, `about-nicolas-lescalier-us.md`, `contact.md` and others.
* Replace or merge the existing `_config.yml` with the updated version that includes Jekyll SEO settings and `title`, `url`, `baseurl` for the `.com` domain.
* Add `robots.txt` and `sitemap.xml` files at the root for crawler directives.
* Commit your changes:

```bash
git add .
git commit -m "Implement U.S. SEO updates and new content"
```

## 3 – Push to GitHub

If working locally, push your branch to GitHub:

```bash
git push origin seo-update-us
```

Open a Pull Request on GitHub and merge into the `main` branch after reviewing.

## 4 – Use the GitHub Web Interface (No CLI)

If you prefer to edit directly in GitHub:

1. Open the repository at `https://github.com/lescalier93/nicolaslescalier`.
2. Click **Add file → Upload files** to drag‑and‑drop or select multiple files from your `us_site` directory.  GitHub will automatically create new folders if they don’t exist.
3. Alternatively, use **Add file → Create new file** and type the path (e.g. `_includes/structured_data.html`) to create directories on the fly.
4. Paste the corresponding content from the prepared files in this package.
5. At the bottom, enter a commit message and choose “Commit directly to the `main` branch” (or open a pull request).

## 5 – Verify Deployment

GitHub Pages automatically builds your site when changes are pushed to `main`.  Monitor the **Actions** tab for build status.  Once successful, visit `https://nicolaslescalier.com` to verify that new pages appear and metadata is visible in the page source.

If you change the custom domain or DNS, update the `CNAME` file in the repository root and adjust DNS records accordingly.

## 6 – Troubleshooting

* **Build Errors** – The Actions log will show any Jekyll errors (e.g. missing layout).  Ensure that all YAML front‑matter fields are properly formatted and that your theme is installed.
* **SSL or DNS Issues** – After updating DNS, it may take several hours for GitHub’s HTTPS certificate to provision.  Check Settings → Pages for domain status.
* **Broken Links** – Run a link checker (e.g. `html-proofer`) locally or use a service like Screaming Frog to identify broken internal/external links.

By following these steps, you can safely deploy the U.S.‑optimized site to GitHub Pages and track results.
