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
| error 404 | [W3C](https://validator.w3.org) | ![screenshot](documentation/testing/html-validation-error404.png) | Pass: validatied by viewing source |
| error 500 | [W3C](https://validator.w3.org) | | Pass: changed "<form class="mt-3" action="{% url 'profile' %}" profile url to cause the error deliberately |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

![CSS DEPLOYED SITE VALIDATION](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fhhwebshop-a59157177b87.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors)
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


