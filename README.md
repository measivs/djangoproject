# Django Project

This is a Django project that consists of two apps, `store` and `order`, which manage products and orders, respectively.

## Project Structure

- **store**: Handles product-related views (list and detail).
- **order**: Manages order-related views.
- **admin**: Django's admin interface for managing the project.

## Views Overview

### `product_list`
- Displays a list of products with links to their respective detail pages.

### `product_detail`
- Displays details of a specific product based on its ID.

### `category_info`
- Provides a JSON response containing information about categories, including their parent categories.

### `product_info`
- Provides a JSON response containing information about products, including their names, image URLs, and related categories.

### `category_listing`
- Renders a list of top-level categories with the quantity of products in each category.

### `product_listing`
- Renders a list of products in a specific category, along with statistical data (max, min, avg prices) and total price of products. Implements pagination for the product list.

### `details_of_product`
- Displays detailed information about a specific product, including its price and description.

## Setup Instructions

### Clone the repository
Clone the project repository using the following command:
```bash
git clone https://github.com/measivs/djangoproject.git
cd djangoproject
