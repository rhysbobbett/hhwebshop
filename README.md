# Hearten Horticulture Webshop

##### **[Click here for the deployed site](https://hhwebshop-a59157177b87.herokuapp.com/)**
-----------------------
The Hearten Horticulture Webshop is an e-commerce store for garden related products. It offers a wide range of tools, seeds and clothing to get started with horticulture. 
The site is easy to use and offers full functionality to purchase goods with a credit or debit card payment. It is a great starting point for any gardener, offering all products for horticulture and garden space DIY tasks.
<br><br>
![amiresponsive](documentation/amiresponsive_screenshot.webp)

## UX

Using Code Institute's Boutique ado project module as a base, I was able to modify parts of the code to suit the requirements of the site.
The site's aim is simplicity for the user to find and purchase a product they require. There is a minimalist layout specifically as gardeners tend to occupy the demographic of an older generation, who are often unfamiliar with the internet and e-commerce in general. They would have no issue in finding a product for their needs based on the navbar's clear layout, or by using the centrally located search bar.

### Colour Scheme

The colours used in the scheme are primarily based on green for plants, blue for water, brown for soil/ground and yellow for sun.
The shades have been lightened or darkened accordingly for their primary usage

- `#628321` : used for primary text.
- `#fffacd` : used for background colour 
- `#6c9dc6` used for secondary text.
- `#4643d` used for secondary highlights.

I used [coolors.co](https://coolors.co/628321-fffacd-6c9dc6-a4643d) to generate my colour palette.

![screenshot](documentation/coolors.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    /* P = Primary | S = Secondary */
    --p-text: #628321;
    --p-highlight: #fffacd;
    --s-text: #6c9dc6;
    --s-highlight: #4643d;
    --white: #FFFFFF;
    --black: #000000;
}
```

### Typography

As the main logo for Hearten Horticulture is written in Barlow Condensed, this will be the main font, with sans serif as a backup.
Lato will be primarily used for sub-headings. Font awesome has been used for some special characters and icons.

- [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) was used for the primary headers and titles.

- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.
