# Django Project

This is a Django project that consists of three apps: `store`, `order`, and `users`. The project manages products, orders, and user accounts.

## Project Structure

- **store**: Handles product-related views (list and detail).
- **order**: Manages order-related views and includes a `UserCart` model for managing user shopping carts.
- **users**: Contains the `User` model for managing user accounts and profiles.
- **admin**: Django's admin interface for managing the project, optimized for better usability.

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
- Renders a list of products in a specific category, along with statistical data (max, min, avg prices) and the total price of products. Implements pagination for the product list.

### `details_of_product`
- Displays detailed information about a specific product, including its price and description.

## Setup Instructions

### Clone the repository
Clone the project repository using the following command:
```bash
git clone https://github.com/measivs/djangoproject.git
cd djangoproject
