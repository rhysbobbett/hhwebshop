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
| Login | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Faccounts%2Flogin%2F#l293c448) | ![screenshot](documentation/testing/html-validation-login.png) | Pass: No Errors |
| Signup / Registration | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Faccounts%2Fsignup%2F#l293c452) | ![screenshot](documentation/testing/html-validation-signup.png) | Errors created by allauth adding an additional <p> tag to the existing code |
| Sign Out | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Faccounts%2Flogout%2F#l293c448) | ![screenshot](documentation/testing/html-validation-signout.png) | Pass: No Errors |
| Profile | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2Fprofile%2F#l293c448) | ![screenshot](documentation/testing/html-validation-profile.png) | Pass: No Errors |
| Error 404 | [W3C](https://validator.w3.org) | ![screenshot](documentation/testing/html-validation-error404.png) | Pass: validatied by viewing source |
| error 500 | [W3C](https://validator.w3.org) | | Pass: changed "<form class="mt-3" action="{% url 'profile' %}" profile url to cause the error deliberately |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

[CSS DEPLOYED SITE VALIDATION](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors)

Testing the  deployed site URL has numerous bootstrap warnings, but there are no errors in my base.css or checkout.css code.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/) | ![screenshot](documentation/testing/base-css.png) | Pass: No Errors, manual input |
| checkout.css | [Jigsaw](https://jigsaw.w3.org/)  | ![screenshot](documentation/testing/base-css.png) | Pass: No Errors, manual input |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/testing/js-validation-countryfield.png) | None |
| stripe_elements.js | ![screenshot](documentation/testing/js-validation-stripe.png) | Undefined Stripe variable |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/manage.py) | ![screenshot](documentation/testing/py-validation-manage.png) | No errors |
| custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/custom_storages.py) | ![screenshot](documentation/testing/py-validation-custom-storages.png) | Pass: No Errors | 
| bag contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/bag/contexts.py) | ![screenshot](documentation/testing/py-validation-custom-storages.png) | Pass: No Errors |
| bag urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/bag/contexts.py) | ![screenshot](documentation/testing/py-validation-custom-storages.png) | Pass: No Errors |
| bag views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/bag/contexts.py) | ![screenshot](documentation/testing/py-validation-custom-storages.png) | Pass: No Errors |
| Checkout admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/admin.py) | ![screenshot](documentation/testing/py-validation-checkout-admin.png) | Pass: No Errors |
| Checkout forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/forms.py) | ![screenshot](documentation/testing/py-validation-checkout-forms.png) | Pass: No Errors |
| Checkout models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/models.py) | ![screenshot](documentation/testing/py-validation-checkout-models.png) | Pass: No Errors |
| Checkout signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/signals.py) | ![screenshot](documentation/testing/py-validation-checkout-signals.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/urls.py) | ![screenshot](documentation/testing/py-validation-checkout-urls.png) | Pass: No Errors  |
| Checkout views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/views.py) | ![screenshot](documentation/testing/py-validation-checkout-views.png) | Pass: No Errors |
| Checkout webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/webhook_handler.py) | ![screenshot](documentation/testing/py-validation-checkout-webhook-handler.png) | Pass: No Errors |
| Checkout webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/checkout/webhooks.py) | ![screenshot](documentation/testing/py-validation-checkout-webhooks.png) | Pass: No Errors |
| hhwebshop settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/hhwebshop/settings.py) | ![screenshot](documentation/testing/py-validation-hhwebshop-settings.png) | Pass: No Errors |
| hhwebshop urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/hhwebshop/settings.py) | ![screenshot](documentation/testing/py-validation-hhwebshop-urls.png) | Pass: No Errors |
| Home urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/home/urls.py) | ![screenshot](documentation/testing/py-validation-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/home/views.py) | ![screenshot](documentation/testing/py-validation-home-views.png) | Pass: No Errors |
| Products admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/admin.py) | ![screenshot](documentation/testing/py-validation-products-admin.png) | Pass: No Errors |
| Products forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/forms.py) | ![screenshot](documentation/testing/py-validation-products-forms.png) | Pass: No Errors |
| Products models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/models.py) | ![screenshot](documentation/testing/py-validation-products-models.png) | Pass: No Errors |
| Products urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/urls.py) | ![screenshot](documentation/testing/py-validation-products-urls.png) | Pass: No Errors |
| Products views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/views.py) | ![screenshot](documentation/testing/py-validation-products-views.png) | Pass: No Errors |
| Products widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/products/widgets.py) | ![screenshot](documentation/testing/py-validation-products-widgets.png) | Pass: No Errors |
| Profiles forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/profiles/forms.py) | ![screenshot](documentation/testing/py-validation-profiles-forms.png) | Pass: No Errors |
| Profiles models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/profiles/models.py) | ![screenshot](documentation/testing/py-validation-profiles-models.png) | Pass: No Errors |
| Profiles urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/profiles/urls.py) | ![screenshot](documentation/testing/py-validation-profiles-urls.png) | Pass: No Errors |
| Profiles views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/rhysbobbett/hhwebshop/main/profiles/views.py) | ![screenshot](documentation/testing/py-validation-profiles-views.png) | 1 TokenError, maybe presense of a non-acsii character |


## Browser Compatibility

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)

| Browser | Home | Products | Product Details | Checkout | Bag | Checkout Success | Add Product | Edit Product | Login | Registration | Sign Out | Profile | Error 404 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browser-chrome-home.png) | ![screenshot](documentation/testing/browser-chrome-products.png) | ![screenshot](documentation/testing/browser-chrome-product-details.png) | ![screenshot](documentation/testing/browser-chrome-checkout.png) | ![screenshot](documentation/testing/browser-chrome-bag.png) | ![screenshot](documentation/testing/browser-firefox-checkout-success.png) | ![screenshot](documentation/testing/browser-chrome-add-product.png) | ![screenshot](documentation/testing/browser-chrome-edit-product.png) | ![screenshot](documentation/testing/browser-chrome-signin.png) | ![screenshot](documentation/testing/browser-chrome-signup.png) | ![screenshot](documentation/testing/browser-chrome-signout.png) | ![screenshot](documentation/testing/browser-chrome-profile.png) | ![screenshot](documentation/testing/browser-chrome-error404.png) | Signout and Error404 text are too obscured |
| Firefox Developer edition | ![screenshot](documentation/testing/browser-firefox-home.png) | ![screenshot](documentation/testing/browser-firefox-products.png) | ![screenshot](documentation/testing/browser-firefox-product-details.png) | ![screenshot](documentation/testing/browser-firefox-checkout.png) | ![screenshot](documentation/testing/browser-firefox-bag.png) | ![screenshot](documentation/testing/browser-firefox-checkout-success.png) | ![screenshot](documentation/testing/browser-firefox-add-product.png) | ![screenshot](documentation/testing/browser-firefox-edit-product.png) | ![screenshot](documentation/testing/browser-firefox-signin.png) | ![screenshot](documentation/testing/browser-firefox-signup.png) | ![screenshot](documentation/testing/browser-firefox-signout.png) | ![screenshot](documentation/testing/browser-firefox-profile.png) | ![screenshot](documentation/testing/browser-firefox-error404.png) | Signout and Error404 text are too obscured |
| Edge | ![screenshot](documentation/testing/browser-edge-home.png) | ![screenshot](documentation/testing/browser-edge-products.png) | ![screenshot](documentation/testing/browser-edge-product-details.png) | ![screenshot](documentation/testing/browser-edge-checkout.png) | ![screenshot](documentation/testing/browser-edge-bag.png) | ![screenshot](documentation/testing/browser-edge-checkout-success.png) | ![screenshot](documentation/testing/browser-edge-add-product.png) | ![screenshot](documentation/testing/browser-edge-edit-product.png) | ![screenshot](documentation/testing/browser-edge-signin.png) | ![screenshot](documentation/testing/browser-edge-signup.png) | ![screenshot](documentation/testing/browser-edge-signout.png) | ![screenshot](documentation/testing/browser-edge-profile.png) | ![screenshot](documentation/testing/browser-edge-error404.png) | as with other browsers, 404 and signout could do with some coloured backing to increase contrast of the fonts |


## Responsiveness
I've tested my deployed project on multiple devices to check for responsiveness issues.
Devtools was used to simulate larger screen sizes with certain devices

| Device | Home | Products | Product Details | Checkout | Bag | Checkout Success | Add Product | Edit Product | Login | Registration | Sign Out | Profile | Error 404 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![Home](documentation/testing/responsiveness-mobile-home.png) | ![Products](documentation/testing/responsiveness-mobile-products.png) | ![Product Details](documentation/testing/responsiveness-mobile-product-details.png) | ![Checkout](documentation/testing/responsiveness-mobile-checkout.png) | ![Bag](documentation/testing/responsiveness-mobile-bag.png) | ![Checkout Success](documentation/testing/responsiveness-mobile-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-mobile-add-product.png) | ![Edit Product](documentation/testing/responsiveness-mobile-edit-product.png) | ![Login](documentation/testing/responsiveness-mobile-login.png) | ![Registration](documentation/testing/responsiveness-mobile-registration.png) | ![Sign Out](documentation/testing/responsiveness-mobile-signout.png) | ![Profile](documentation/testing/responsiveness-mobile-profile.png) | ![Error 404](documentation/testing/responsiveness-mobile-error404.png) | The sign out text and error404 text are too dark against the green of the background, the page should be made so it adapts when the error folder is referenced or the account page is referenced |
| Tablet (DevTools - iPad Air) | ![Home](documentation/testing/responsiveness-tablet-home.png) | ![Products](documentation/testing/responsiveness-tablet-products.png) | ![Product Details](documentation/testing/responsiveness-tablet-product-details.png) | ![Checkout](documentation/testing/responsiveness-tablet-checkout.png) | ![Bag](documentation/testing/responsiveness-tablet-bag.png) | ![Checkout Success](documentation/testing/responsiveness-tablet-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-tablet-add-product.png) | ![Edit Product](documentation/testing/responsiveness-tablet-edit-product.png) | ![Login](documentation/testing/responsiveness-tablet-login.png) | ![Registration](documentation/testing/responsiveness-tablet-registration.png) | ![Sign Out](documentation/testing/responsiveness-tablet-signout.png) | ![Profile](documentation/testing/responsiveness-tablet-profile.png) | ![Error 404](documentation/testing/responsiveness-tablet-error404.png) | The iPad devtools view provides a wider display of products than mobile view, but still is compact due to the collapsible navbar.  |
| Desktop | ![Home](documentation/testing/responsiveness-desktop-home.png) | ![Products](documentation/testing/responsiveness-desktop-products.png) | ![Product Details](documentation/testing/responsiveness-desktop-product-details.png) | ![Checkout](documentation/testing/responsiveness-desktop-checkout.png) | ![Bag](documentation/testing/responsiveness-desktop-bag.png) | ![Checkout Success](documentation/testing/responsiveness-desktop-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-desktop-add-product.png) | ![Edit Product](documentation/testing/responsiveness-desktop-edit-product.png) | ![Login](documentation/testing/responsiveness-desktop-signin.png) | ![Registration](documentation/testing/responsiveness-desktop-signup.png) | ![Sign Out](documentation/testing/responsiveness-desktop-signout.png) | ![Profile](documentation/testing/responsiveness-desktop-profile.png) | ![Error 404](documentation/testing/responsiveness-desktop-error404.png) | This has the been the most often used resolution for the development of the site and works across the pages |
| XL Monitor (Devtools) | ![Home](documentation/testing/responsiveness-xl-monitor-home.png) | ![Products](documentation/testing/responsiveness-xl-monitor-products.png) | ![Product Details](documentation/testing/responsiveness-xl-monitor-product-details.png) | ![Checkout](documentation/testing/responsiveness-xl-monitor-checkout.png) | ![Bag](documentation/testing/responsiveness-xl-monitor-bag.png) | ![Checkout Success](documentation/testing/responsiveness-xl-monitor-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-xl-monitor-add-product.png) | ![Edit Product](documentation/testing/responsiveness-xl-monitor-edit-product.png) | ![Login](documentation/testing/responsiveness-xl-monitor-signin.png) | ![Registration](documentation/testing/responsiveness-xl-monitor-signup.png) | ![Sign Out](documentation/testing/responsiveness-tablet-signout.png) | ![Profile](documentation/testing/responsiveness-xl-monitor-profile.png) | ![Error 404](documentation/testing/responsiveness-tablet-error404.png) | Pages appear to all view correctly as intended |
| 4K Monitor (Devtools) | ![Home](documentation/testing/responsiveness-4k-monitor-home.png) | ![Products](documentation/testing/responsiveness-4k-monitor-products.png) | ![Product Details](documentation/testing/responsiveness-4k-monitor-product-details.png) | ![Checkout](documentation/testing/responsiveness-4k-monitor-checkout.png) | ![Bag](documentation/testing/responsiveness-4k-monitor-bag.png) | ![Checkout Success](documentation/testing/responsiveness-4k-monitor-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-4k-monitor-add-product.png) | ![Edit Product](documentation/testing/responsiveness-4k-monitor-edit-product.png) | ![Login](documentation/testing/responsiveness-4k-monitor-signin.png) | ![Registration](documentation/testing/responsiveness-4k-monitor-signup.png) | ![Sign Out](documentation/testing/responsiveness-4k-monitor-signout.png) | ![Profile](documentation/testing/responsiveness-4k-monitor-profile.png) | ![Error 404](documentation/testing/responsiveness-4k-monitor-error404.png) | My profile page doesn't display in devtools on my display unless I view it zoomed out to 50%, other pages could be better optimised for 4k as a future update. |
| Google Pixel 7 | ![Home](documentation/testing/responsiveness-pixel7-home.png) | ![Products](documentation/testing/responsiveness-pixel7-products.png) | ![Product Details](documentation/testing/responsiveness-pixel7-product-details.png) | ![Checkout](documentation/testing/responsiveness-pixel7-checkout.png) | ![Bag](documentation/testing/responsiveness-pixel7-bag.png) | ![Checkout Success](documentation/testing/responsiveness-pixel7-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-pixel7-add-product.png) | ![Edit Product](documentation/testing/responsiveness-pixel7-edit-product.png) | ![Login](documentation/testing/responsiveness-pixel7-signin.png) | ![Registration](documentation/testing/responsiveness-pixel7-signup.png) | ![Sign Out](documentation/testing/responsiveness-pixel7-signout.png) | ![Profile](documentation/testing/responsiveness-pixel7-profile.png) | ![Error 404](documentation/testing/responsiveness-pixel7-error404.png) | All pages displayed correctly and visible apart from error404. |
| iPhone 14 | ![Home](documentation/testing/responsiveness-iphone14-home.png) | ![Products](documentation/testing/responsiveness-iphone14-products.png) | ![Product Details](documentation/testing/responsiveness-iphone14-product-details.png) | ![Checkout](documentation/testing/responsiveness-iphone14-checkout.png) | ![Bag](documentation/testing/responsiveness-iphone14-bag.png) | ![Checkout Success](documentation/testing/responsiveness-iphone14-checkout-success.png) | ![Add Product](documentation/testing/responsiveness-iphone14-add-product.png) | ![Edit Product](documentation/testing/responsiveness-iphone14-edit-product.png) | ![Login](documentation/testing/responsiveness-iphone14-signin.png) | ![Registration](documentation/testing/responsiveness-iphone14-signup.png) | ![Sign Out](documentation/testing/responsiveness-iphone14-signout.png) | ![Profile](documentation/testing/responsiveness-iphone14-profile.png) | ![Error 404](documentation/testing/responsiveness-iphone14-error404.png) | As with the first mobile view, the signout text is too dark against the green background image and will need to be changed |

## Lighthouse Audit

The site's image size, organisation and retrieval of information makes it slow to load, and performance suffers on any page featuring a static image file.

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse-home-mobile.png) | ![screenshot](documentation/testing/lighthouse-home-desktop.png) | Mobile performance suffers due to images |
| Products | ![screenshot](documentation/testing/lighthouse-products-mobile.png) | ![screenshot](documentation/testing/lighthouse-products-desktop.png) | Slow response time due to large images |
| Product Details | ![screenshot](documentation/testing/lighthouse-product-details-mobile.png) | ![screenshot](documentation/testing/lighthouse-product-details-desktop.png) | Slow response time due to large images |
| Bag | ![screenshot](documentation/testing/lighthouse-bag-mobile.png) | ![screenshot](documentation/testing/lighthouse-bag-desktop.png) | Slow response time due to large images |
| Checkout Success | ![screenshot](documentation/testing/lighthouse-checkout-success-mobile.png) | ![screenshot](documentation/testing/lighthouse-checkout-success-desktop.png) | Slow response time due to large images |
| Add Product | ![screenshot](documentation/testing/lighthouse-add-product-mobile.png) | ![screenshot](documentation/testing/lighthouse-add-product-desktop.png) | Mobile performance suffers due to images |
| Edit Product | ![screenshot](documentation/testing/lighthouse-edit-product-mobile.png) | ![screenshot](documentation/testing/lighthouse-edit-product-desktop.png) | Mobile performance suffers due to images |
| Login | ![screenshot](documentation/testing/lighthouse-signin-mobile.png) | ![screenshot](documentation/testing/lighthouse-signin-desktop.png) | Mobile performance suffers due to images  |
| Signup / Registration | ![screenshot](documentation/testing/lighthouse-signup-mobile.png) | ![screenshot](documentation/testing/lighthouse-signup-desktop.png) | Mobile performance suffers due to images |
| Sign Out | ![screenshot](documentation/testing/lighthouse-signout-mobile.png) | ![screenshot](documentation/testing/lighthouse-signout-desktop.png) | Mobile performance suffers due to images |
| Profile | ![screenshot](documentation/testing/lighthouse-profile-mobile.png) | ![screenshot](documentation/testing/lighthouse-profile-desktop.png) | Mobile performance suffers due to images |

## Defensive Programming

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses
- User passwords must not contain reference to name or username, must contain numbers.
- User must state a country in checkout

Django:
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| Shop now button | Clickinig the button takes a user to all products | Clicked the button to test, takes me to products | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/home-feature01.png) |
| Search Box | Anything can be put in the search box, but putting nothing in will bring up all products | Tested the feature by clicking with no text | The feature responded as expected | Test concluded and passed | ![screenshot](documentation/testing/home-feature02.png) |
| Products | | | | | |
| The products can be sorted by various categories (a=z, price, rating)  | The filter was selected from the dropdown and resorts the products accordingly | Tested the feature by changing sort categories | The feature behaved as expected, and it sorts as described | Test concluded and passed | ![screenshot](documentation/testing/products-feature01.png) |
| Verify product filtering with specific criteria | When a tag is clicked, all products are filtered to that specific category | Tested the feature by clicking 'herbs' | Worked as expected, all herbs populate the products page | Test concluded, passed | ![screenshot](documentation/testing/products-feature02.png) |
| Product Details | | | | | |
| Product quantity cannont be less than 1 | a notification should appear if less than 1 is entered in quantity | Tested the feature by entering 0 | The feature behaved as expected, and it did provided the notification | Test concluded and passed | ![screenshot](documentation/testing/products-details-feature02.png) |
| Special offers within product details | Feature is expected to filter all products in that given category by their special offer tag stated in the product description | Tested the feature clicking the offer tag | The product filter than categories according to subcategory and which special offer has been clicked | This could be developed further for more control over product filtering | ![screenshot](documentation/testing/products-details-feature02.png) |
| Add product | | | | | |
| Essential forms require data | Feature is expected to provide notification when the user does not enter into a form such as name, price and description | Tested the feature by doing not entering data into the fields | The feature behaved as expected, and it provided notification that it is a required field. It does this for all essential fields | Test concluded and passed | ![screenshot](documentation/testing/add-product-feature01.png) |
| image upload | Feature is expected to upload an image when the user clicks upload | Tested the feature by uploading an image | The image appears in the product details | I tested by uploading a favicon.ico image for convenience but other images work. | ![screenshot](documentation/testing/add-product-feature02.png) |
| Edit product | | | | | |
| Edit a product details | Feature is expected to do update details on button click if a user changes any existing details | Tested the feature by editting the product in the add-product features section above | The feature behaved as expected, and it did update the relevant fields | Test concluded and passed | ![screenshot](documentation/testing/edit-product-feature01.png) |
| Edit a product image | Feature is expected to do update details on button click if a user changes the existing image in the upload preview section | Tested the feature by editting the product in the add-product features section above, updating the image to something else | The feature behaved as expected, and it did update the relevant image | Test concluded and passed, screenshot is post-edit on the edit-product page | ![screenshot](documentation/testing/edit-product-feature02.png) |
| Checkout | | | | | |
| Name field is required | Feature is expected to give a notification when blank | Tested the feature by leaving name field blank | The feature behaved as expected, and it provided the notification and would not proceed without it | Test concluded and passed, this applies to the email field, phone number, address and credit card fields also | ![screenshot](documentation/testing/checkout-feature01.png) |
| Order email to sent from the business email address, user receives order confirmation email | Feature is expected to send email upon completion when the user makes a purchase | Tested the feature by placing an order | The feature behaved as expected, and it sent the email order notification | Test concluded and passed | ![screenshot](documentation/testing/checkout-success-feature01.png) |
| Profile | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/testing/profile-feature01.png) |
| Signup | | | | | |
| Enter correct email | Feature is expected to display to the user that an email address is require to signup | Tested the feature by mistyping email in email address form | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/signup-feature01.png) |
| Username must be a minimum length | Feature is expected to display notification when the user does enter a long enough username. | Tested the feature by entering too short a username | The feature works as intended | I did Z to the code because something was missing | ![screenshot](documentation/testing/signup-feature02.png) |
| Sign in | | | | | |
| Sign in page displaying correctly | Feature is expected to appear when the user clicks signin on the navbar | Tested the feature by clicking signin | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/signin-feature01.png) |
| No user found | Feature is expected to display a error when the user enters a name not found in the system | Tested the feature by entering a wrong username | The feature works as intended | Tested passed | ![screenshot](documentation/testing/signin-feature02.png) |
| Sign out| | | | | |
| Signing out with a button | Feature is expected to do signout when the user clicks to signout | Tested the feature by attempting a signout | The feature behaved as expected, and it did have any issues | Test concluded and passed | ![screenshot](documentation/testing/signout-feature01.png) ||
| Error 404| | | | | |
| Page not found | Feature is expected to display Page not found test when the user types an incorrect url | Tested the feature by deliberately calling the 404 page. | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/testing/error404-feature01.png) |


## User Story Testing

| User Story | Screenshot 1 | Screenshot 2 | Screenshot 3 |
| --- | --- | --- | --- |
| As a new site user, I would like to create an account easily, so that I can save my preferences, view my order history, and manage my shipping information. | ![screenshot](documentation/testing/new-user-feature01.png) | ![screenshot](documentation/testing/new-user-feature02.png) |  ![screenshot](documentation/testing/new-user-feature03.png) |
As a new site user, I would like to search for plants or tools by their names or categories to explore available options. | ![screenshot](documentation/testing/new-user-feature04.png) | ![screenshot](documentation/testing/new-user-feature05.png) | ![screenshot](documentation/testing/new-user-feature06.png)
| As a new site user, I would like to add items to my shopping cart and proceed to checkout to purchase the selected products. I should be able to edit the quantity of items if I make a mistake | ![screenshot](documentation/testing/new-user-feature07.png) | ![screenshot](documentation/testing/new-user-feature08.png) | ![screenshot](documentation/testing/new-user-feature09.png) |
| As a returning site user, I would like to access my order history to review past purchases. | ![screenshot](documentation/testing/return-user-feature01.png) | 
| As a returning site user, I would like to receive a confirmation email after placing my order for reference and tracking purposes. | ![screenshot](documentation/testing/return-user-feature02.png) |
| As a site administrator, I should be able to manage user accounts and permissions, so that I can control access levels and ensure site security. | ![screenshot](documentation/testing/site-admin-feature01.png) |
| As a site administrator, I should be able to update and add new product listings, so that I can keep the site content current and attractive to customers. | ![screenshot](documentation/testing/site-admin-feature02.png) |

## Bugs
The development has shown any problem bugs that have inhibited the main functionality of the site.
I saved one bug early on in Issues, but have yet to find a solution to this. It is a minor issue that doesn't affect the running of the site. 

- During development I encountered a few issues with deployment that were due to simple typos within the heroku env config variables.
    
    - These were fixed by providing the correct variables in the heroku config fields, and double checking their spelling and format.

- When using devtools to simulate an iPad Pro, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/testing/unfixed-bug01.png)

    - Attempted fix: a rewrite of my media queries maybe required in order to fix this issue as it appears to have conflicts with other essential elements such as the Stripe payments overlay.

- Django Allauth is adding an unnecessary < p > < /p > tag which causes the HTML validation to error.
    
    - Attempted search for a solution: screenshots are noted in the issues section of the repository, this is believed to be allauth adding a < p > tag and for now is not a fix I understand how to solve.

There are no remaining bugs that I am aware of.