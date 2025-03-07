import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ph_units",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
