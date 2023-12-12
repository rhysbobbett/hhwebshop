# Testing

Return back to the [README.md](README.md) file.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2F) | ![screenshot](documentation/testing/html-validation-home.png) | Pass |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fproducts%2Fproducts) | ![screenshot](documentation/testing/html-validation-products.png) | Pass |
| Product Details | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fproducts%2F1%2F) | ![screenshot](documentation/testing/html-validation-product-details.png) | Pass |
| Checkout | [W3C](https://validator.w3.org/nu/#textarea) | ![screenshot](documentation/testing/html-validation-checkout.png) | Pass: 3 errors shown are created by stripe, check required validation by input as an error occurs otherwise |
| Bag | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fbag%2F#l312c63) | ![screenshot](documentation/testing/html-validation-bag.png) | Pass: No Errors |
| Checkout Success | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fcheckout%2Fcheckout_success%2FECD84BE070E84329BF9BAE2D76CC96C5#l312c63) | ![screenshot](documentation/testing/html-validation-checkout-success.png) | Pass: No Errors |
| Add Product | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fproducts%2Fadd%2F#l312c63) | ![screenshot](documentation/testing/html-validation-add-product.png) | Pass: Gives info on a trailing slash but it doesn't appear to be from my code |
| Edit Product | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fproducts%2Fedit%2F7%2F#l312c63) | ![screenshot](documentation/testing/html-validation-edit-product.png) | Pass: Gives info on a trailing slash but it doesn't appear to be from my code |
