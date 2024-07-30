# Queuing System Project

This project implements a queuing system using JavaScript, Express, and Redis to manage product reservations efficiently. The application provides a simple RESTful API for listing products and reserving them based on stock availability.

## Features

- List all available products with details such as ID, name, price, and stock quantity.
- Retrieve detailed information about a specific product by ID.
- Reserve a product if stock is available, with appropriate handling for out-of-stock scenarios.
- Utilize Redis for efficient stock management.

## Technologies Used

- JavaScript (Node.js)
- Express.js
- Redis
- JSON for data interchange

## Project Structure

### Product Data

An array named `listProducts` contains product details in the following format:

```javascript
const listProducts = [
    { id: 1, name: "Product A", price: 100, stock: 10 },
    { id: 2, name: "Product B", price: 150, stock: 5 },
    // Add more products as needed
];
```

### API Endpoints

- **GET /list_products**
  - Returns a JSON array of all available products.

- **GET /list_products/:itemId**
  - Returns detailed information about a specific product, including its current stock levels.

- **GET /reserve_product/:itemId**
  - Reserves the product if stock is available and responds accordingly:
    - Success message if reserved.
    - Out-of-stock notification if no stock is available.
    - Error message if the product does not exist.

## Setting Up the Server

1. Clone the repository to your local machine.
2. Install the necessary dependencies:

```bash
npm install express redis
```

3. Set up and run the Redis server if you haven't done so already.
4. Start the Express server:

```bash
node index.js
```

5. The server will listen on `http://localhost:1245`.

## Usage

### Listing Products

To fetch the list of products, navigate to:

```
GET http://localhost:1245/list_products
```

### Product Details

To get details of a specific product, use:

```
GET http://localhost:1245/list_products/:itemId
```

Replace `:itemId` with the actual product ID.

### Reserving a Product

To reserve a product, send a request to:

```
GET http://localhost:1245/reserve_product/:itemId
```

## Error Handling

The application includes error handling for:

- Non-existent products.
- Insufficient stock levels.

## Questions for Further Consideration

- How can the product reservation process be improved for better user experience?
- What are the advantages of using Redis for stock management in this application?
- What are the best practices for handling errors in Express applications?

## License

This project is licensed under the MIT License.
