from setuptools import setup


setup(
    name="Star_Light-tk",
    version="1.0.0",
    description="Software for Astronomical calculations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Islamtrabeih/Star_Light-tk",
    author="Islam-Trabeih | Rahma-Ashraf",
    author_email="islamtrabeih.me@gmail.com",
    license="FOSS",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",],
    packages=["star_tk"],
    include_package_data=True,
    install_requires=["plotly", "pandas", "tkinter", "ttkkthemes"],
    entry_points={"console_scripts": ["star=star_tk.GUI"]},
)
