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

## Features

### Multi-Page Features: 
### Navigation

#### Top Navigation:
The top navigation serves as a hub for essential site functions. Here's what it offers:

#### Logo & Search Bar: 
Easily spot the site's logo for brand recognition and use the search bar to explore products.

#### Login/Register: 
Access the "My Account" icon for a seamless login or registration experience.

#### Shopping Bag: 
Monitor the shopping bag's contents conveniently.

#### User-Specific Dropdown: 
Once logged in, the dropdown menu within "My Account" dynamically adjusts based on the user's role—Shop Owners/Administrators access "Product Management" while shoppers navigate to "My Profile". The "Log Out" option ensures smooth user management.

#### Main Navigation:
Accessible via the hamburger icon on mobile devices, the main navigation focuses on:

Product Categories: Delve into diverse product categories for a comprehensive exploration.
Responsive Design:
The website prioritizes responsiveness across devices. Check out these screenshots showcasing the design's adaptability:

Navbar - Desktop
Navbar - Mobile
My Account - Logged out
My Account - Shopper
My Account - Shop Owner/Administrator
This deliberate design strategy aims for intuitive interactions and responsiveness, ensuring a seamless browsing journey for all users, regardless of their device or screen size.

### Footer

The footer, a consistent feature across all pages, plays a vital role, especially for mobile users who might find the navbar logo less accessible on smaller screens. Here's what it comprises:

Direct Navigation: Offers convenient access to the homepage, prioritizing ease of navigation for mobile users.

"About Us" Section: Presents a concise overview of the store's mission or purpose, providing users with essential insights.

Social Media Links: Enables users to connect with the brand across various platforms, staying updated on news and promotions.

Payment Disclaimer: Notably includes a disclaimer regarding payments processed through Stripe, clarifying that these transactions occur in test mode. This transparency sets clear user expectations during transactions.

In summary, the footer stands as a structured and informative segment, enhancing the user experience by facilitating easy access to crucial information and navigation options. Additionally, the inclusion of the payment disclaimer reinforces trust and transparency in the payment process.

Footer - Desktop
This component ensures a consistent and user-friendly experience across devices, emphasizing accessibility and clarity for all users.


### Existing Features

#### User Account Creation
The user account creation feature enables new visitors to sign up easily. It provides them with personalized experiences, such as saving preferences, accessing order history, and managing shipping information. For the gardening enthusiasts visiting the site, this feature ensures a tailored shopping experience and efficient management of their gardening needs.

![screenshot](documentation/feature01-signup.png)

#### Product search
The product search and filtering functionality allow users to find specific plants or gardening tools based on price range. This feature caters to users who are looking for precise gardening items, making their shopping process seamless and efficient.

![screenshot](documentation/feature02-search.png)

#### Basket / Bag
The basket allows users to easily adjust quantity or remove the products, it provides a running sub-total with delivery charge tallied below it.

![screenshot](documentation/feature05-bag.png)

#### Secure Checkout
The secure checkout process ensures a safe and hassle-free transaction for customers. It displays clear information about shipping costs, payment methods, and estimated delivery times, providing a smooth and trustworthy experience for users who are ready to make purchases.

![screenshot](documentation/feature03-checkout.png)

#### Order History and Reordering
The order history feature allows returning users to track their past purchases and easily reorder items they've previously bought. It caters to users who want a convenient reference for their gardening needs, enabling them to replicate successful past purchases effortlessly.

![screenshot](documentation/feature04-orderhistory.png)

### Future Features

#### Garden Planner Tool

A digital garden planner that allows users to design and plan their gardens virtually. Users can drag and drop plants, visualize their layout, and receive recommendations based on their selected plants and garden conditions. This feature would cater to users who want assistance in planning and organizing their garden spaces effectively.

#### Community Forum or Garden Sharing Platform
An interactive community platform where users can share gardening tips, experiences, and even trade or sell plants among themselves. This feature would encourage engagement among gardening enthusiasts, fostering a sense of community and knowledge-sharing.

#### Seasonal Plant Care Reminders
A personalized notification system that sends users reminders and tips for seasonal plant care based on the plants they have purchased or favorited. This feature would assist users in maintaining healthy plants throughout the year by providing timely care advice tailored to their specific plants.

#### Virtual Plant Consultation
A feature that offers users the option to schedule virtual consultations with gardening experts or botanists. Users can seek personalized advice on plant care, garden design, or troubleshooting specific issues they encounter with their plants. This feature would provide valuable guidance for users seeking professional expertise in their gardening endeavors.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

## Database Design

```python
class Product(models.Model):
    class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True) # noqa
    special_offer = models.ForeignKey(SpecialOffer, blank=True, on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # noqa
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```

![screenshot](documentation/erd.png)

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://hhwebshop-a59157177b87.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: hhwebshop).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-hhwebshop` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-hhwebshop` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for hhwebshop static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-hhwebshop".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-hhwebshop") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-hhwebshop` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-hhwebshop`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://hhwebshop-a59157177b87.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or hhwebshop
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/rhysbobbett/hhwebshop) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/rhysbobbett/hhwebshop.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/rhysbobbett/hhwebshop)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/rhysbobbett/hhwebshop)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits



| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

All product images are from Amazon, Thompson & Morgan seeds and the tool companies that are identifiable in the relavent images. These images are for this project only and are only to be used for educational purposes.
Additional images (such as the background) were created by me using Stable Diffusion AI on my own PC.

### Acknowledgements
- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner Catherine, for believing in me, and allowing me to make this transition into software development.

