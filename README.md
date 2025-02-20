# GitHub landing page

The [`profile/README.md`](profile/README.md) file in this repository is the
[landing page](https://github.com/saezlab) for the `saezlab` GitHub
organization. Do not edit that file directly. Instead, read the guide below how
to edit the landing page.

## How to edit

1. Install [poetry](https://python-poetry.org/) if you don't have it already
   installed
2. Create the `poetry` environment required to run the Python script generating
   the markdown for the landing page by running `poetry install`
3. Do your edits:
   - The main text can be edited in
     [`profile/src/README.main.md`](profile/src/README.main.md)
   - The resources are defined in
     [`profile/src/resources.yaml`](profile/src/resources.yaml). To add a new
     resource, include the logo in the `profile/logos` directory by the name of
     the resource all lowercase, in `svg` or `png` format. For example, for
     OmniPath we have `omnipath.svg`. Then add the name, title and URLs of the
     resource in `resources.yaml`. And also include the name of the resource in
     the list at the top of the file. By removing a name from the list, a
     resource can be hidden while still keeping its information in the `yaml`.
     Each link has a type, see the possible types below. For links to packages,
     add a suffix to the URL type, such as `package:PYPI` or `package:BIOC`,
     for PyPI and Bioconductor respectively.

     | Link type   | For links to...      |
     | ----------- | -------------------- |
     | `home`      | Homepage             |
     | `python`    | Python repository    |
     | `r`         | R repository         |
     | `package`   | Package              |
     | `docs-py`   | Python documentation |
     | `docs-r`    | R documentation      |
     | `article`   | Publication          |
     | `main`      | Link for the logo (to override the default) |

   - The footer of the landing page (anything after the table) can be edited in
     [`profile/src/README.foot.md`](profile/src/README.foot.md)
4. Run the [`profile/src/update_md.py`](profile/src/update_md.py) script to
   generate the landing page, i.e. the `profile/README.md` file:
   `poetry run profile/src/update_md.py`.
5. Check by `grip`, the GitHub-identical markdown renderer, whether your
   updates are correct. If you added a new image, it won't be visible yet,
   because the images are referenced by their absolute URLs under `github.com`.
   Run `poetry run grip profile/README.md` and open the test server in the
   browser.
5. Commit and push your changes. Check if the updates are shown correctly.
   Don't forget, you see a different page depending on whether you are logged
   in with an account in the `saezlab` GitHub organization.
6. Finally, cross-merge your changes between the
   [`.github`](https://github.com/saezlab/.github) and
   [`.github-private`](https://github.com/saezlab/.github-private), by adding
   the one you edited to the other one as a new remote, fetching and merging
   it, and then force push it to the remote.
