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

## User Stories

- As a user, I want to create an account easily so that I can save my preferences, view my order history, and manage my shipping information.
- As a user, I want to search for plants or tools by their names or categories to explore available options.
- As a user, I want to add items to my shopping cart and proceed to checkout to purchase the selected products.
- As a user, I want to access my order history to review past purchases
- As a user, I want to receive a confirmation email after placing my order for reference and tracking purposes.

### New Site Users

- As a new site user, I would like to create an account, so that I can save my preferences, track my orders, and easily manage my information.
- As a new site user, I would like to explore a variety of plants and gardening tools, so that I can make informed decisions about what suits my gardening needs.
- As a new site user, I would like to have a simple and intuitive navigation system, so that I can easily find what I'm looking for without feeling overwhelmed.
- As a new site user, I would like to access customer support easily, so that I can get assistance whenever I have questions or encounter issues while using the site.
- As a new site user, I would like to read reviews and ratings from other customers, so that I can make more informed decisions about the quality and suitability of plants and gardening products before making a purchase.

### Returning Site Users

- As a returning site user, I would like to access my previous order history, so that I can track my past purchases and easily reorder items.
- As a returning site user, I would like to update my saved shipping addresses, so that I can efficiently send gifts or order items for different locations.
- As a returning site user, I would like to easily connect with customer support, so that I can receive assistance or address any issues promptly.

### Site Admin

- As a site administrator, I should be able to manage user accounts and permissions, so that I can control access levels and ensure site security.
- As a site administrator, I should be able to update and add new product listings, so that I can keep the site content current and attractive to customers.
- As a site administrator, I should be able to monitor and respond to customer feedback or reviews, so that I can maintain a positive user experience and address any issues promptly.
- As a site administrator, I should be able to configure and maintain the site's backend infrastructure, so that I can ensure smooth site functionality and address any technical issues that arise.

## Wireframes

To follow best practice, the wireframes for the site were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/home_mobile.png)

Products
  - ![screenshot](documentation/wireframes/products_mobile.png)

Product details
  - ![screenshot](documentation/wireframes/productdetails_mobile.png)

Registration
  - ![screenshot](documentation/wireframes/registration_mobile.png)

My Profile
  - ![screenshot](documentation/wireframes/profile_mobile.png)

Sign in 
  - ![screenshot](documentation/wireframes/login_mobile.png)

Sign out
  - ![screenshot](documentation/wireframes/signout_mobile.png)

Bag 
  - ![screenshot](documentation/wireframes/bag_mobile.png)

Checkout Success
  - ![screenshot](documentation/wireframes/checkoutsuccess_mobile.png)

Add a product
  - ![screenshot](documentation/wireframes/addproduct_mobile.png)

Edit a product
  - ![screenshot](documentation/wireframes/editproduct_mobile.png)

</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>
Home
  - ![screenshot](documentation/wireframes/home_tablet.png)

Products
  - ![screenshot](documentation/wireframes/products_tablet.png)

Product details
  - ![screenshot](documentation/wireframes/productsdetails_tablet.png)

Registration
  - ![screenshot](documentation/wireframes/registration_tablet.png)

My Profile
  - ![screenshot](documentation/wireframes/profile_tablet.png)

Sign in 
  - ![screenshot](documentation/wireframes/login_tablet.png)

Sign out
  - ![screenshot](documentation/wireframes/signout_tablet.png)

Bag 
  - ![screenshot](documentation/wireframes/bag_tablet.png)

Checkout Success
  - ![screenshot](documentation/wireframes/checkoutsuccess_tablet.png)

Add a product
  - ![screenshot](documentation/wireframes/addproduct_tablet.png)

Edit a product
  - ![screenshot](documentation/wireframes/editproduct_tablet.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/home_desktop.png)

Products
  - ![screenshot](documentation/wireframes/products_desktop.png)

Product details
  - ![screenshot](documentation/wireframes/productdetails_desktop.png)

Registration
  - ![screenshot](documentation/wireframes/registration_desktop.png)

My Profile
  - ![screenshot](documentation/wireframes/profile_desktop.png)

Sign in 
  - ![screenshot](documentation/wireframes/login_desktop.png)

Sign out
  - ![screenshot](documentation/wireframes/signout_desktop.png)

Bag 
  - ![screenshot](documentation/wireframes/bag_desktop.png)

Checkout Success
  - ![screenshot](documentation/wireframes/checkoutsuccess_desktop.png)

Add a product
  - ![screenshot](documentation/wireframes/addproduct_desktop.png)

Edit a product
  - ![screenshot](documentation/wireframes/editproduct_desktop.png)


</details>

