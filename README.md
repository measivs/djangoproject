# Django Project

This is a Django project that consists of two apps, `store` and `order`, which manage products and orders, respectively.

## Project Structure

- **store**: Handles product-related views (list and detail).
- **order**: Manages order-related views.
- **admin**: Django's admin interface for managing the project.

## Features

### Store App
- **Product List**: Displays a list of available products with links to their details.
- **Product Detail**: Shows detailed information about a specific product.
- **Category Information**: Provides a list of all categories in JSON format.
- **Product Information**: Exports product data, including their related categories, in JSON format.

### Order App
- **Order List**: Displays a list of customer orders.
- **Order Detail**: Shows detailed information about a specific order, including the product, quantity, and total price.

## Setup Instructions

### Clone the repository
Clone the project repository using the following command:
```bash
git clone https://github.com/measivs/djangoproject.git
cd djangoproject
