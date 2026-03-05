# QuickCart API Documentation
---
## How to run the Server
1. Make sure to install [Docker/Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Use the command ``docker load -i quickcart_image.tar`` to load the docker Image
3. Use the command ``docker run -p 8080:8080 quickcart`` inorder to run the server. You would see a link to access the server.

## Note
- The documentation is a bit ambiguous since we would like you to guess what would be the input and output given that you know what each API does. For the ones which we felt would be hard to figure out, we have added hints.
- A good idea to approach the assignment would to use tools like [Postman](https://www.postman.com/downloads/) to get a hang of the System and then write the testcases.
- Please do mail at george.rahul@research.iiit.ac.in incase there are any issues with Server (at least one week before the deadline)
## All Requests

Every request must include an `X-Roll-Number` header containing a valid integer. If it is missing, the server returns a 401 error. If the header value is not a valid integer (e.g. letters or symbols), the server returns a 400 error.

All user-scoped endpoints also require an `X-User-ID` header containing a positive integer matching an existing user. If it is missing or invalid, the server returns a 400 error. Admin endpoints (`/admin/*`) do not require this header.

---

## Admin / Data Inspection

APIs: `GET /api/v1/admin/users`, `GET /api/v1/admin/users/{user_id}`, `GET /api/v1/admin/carts`, `GET /api/v1/admin/orders`, `GET /api/v1/admin/products`, `GET /api/v1/admin/coupons`, `GET /api/v1/admin/tickets`, `GET /api/v1/admin/addresses`

These endpoints return full database contents and are not scoped to a single user. They are useful for verifying state during testing. All require the `X-Roll-Number` header.

- `GET /api/v1/admin/users` returns all users with their wallet balances and loyalty points.
- `GET /api/v1/admin/users/{user_id}` returns one specific user.
- `GET /api/v1/admin/carts` returns every cart with all items and computed totals.
- `GET /api/v1/admin/orders` returns all orders across all users, including payment and order status.
- `GET /api/v1/admin/products` returns all products including those marked inactive.
- `GET /api/v1/admin/coupons` returns all coupons including expired ones with their discount rules.
- `GET /api/v1/admin/tickets` returns all support tickets across all users.
- `GET /api/v1/admin/addresses` returns all addresses across all users.

---

## Profile

APIs: `GET /api/v1/profile`, `PUT /api/v1/profile`

The user can get their profile and update it.

When updating, the name must be between 2 and 50 characters. The phone number must be exactly 10 digits. If either rule is broken, the server returns a 400 error.

---

## Addresses

APIs: `GET /api/v1/addresses`, `POST /api/v1/addresses`, `PUT /api/v1/addresses/{address_id}`, `DELETE /api/v1/addresses/{address_id}`

The user can add, view, update, and delete addresses.

When adding an address, the label must be HOME, OFFICE, or OTHER. The street must be between 5 and 100 characters. The city must be between 2 and 50 characters. The pincode must be exactly 6 digits. If any of these rules are broken, the server returns a 400 error.

A successful POST returns a message and the full address object that was just created, including its assigned address_id, label, street, city, pincode, and is_default fields.

When a new address is added as the default, all other addresses must stop being the default first. Only one address can be default at a time.

When updating an address, only the street and the is_default field can be changed. Label, city, and pincode cannot be changed through the update endpoint.

When an address is updated, the response must show the new updated data, not the old data.

Deleting an address that does not exist returns a 404 error.

---

## Products

APIs: `GET /api/v1/products`, `GET /api/v1/products/{product_id}`

The user can get a list of all products or look up one product by its ID.

The product list only returns products that are active. Inactive products are never shown in the list.

Looking up a single product by ID returns a 404 error if the product does not exist.

Products can be filtered by category, searched by name, and sorted by price going up or down.

The price shown for every product must be the exact real price stored in the database.

---

## Cart

APIs: `GET /api/v1/cart`, `POST /api/v1/cart/add`, `POST /api/v1/cart/update`, `POST /api/v1/cart/remove`, `DELETE /api/v1/cart/clear`

The user can view the cart, add items, update quantities, remove items, and clear the whole cart.

When adding an item, the quantity must be at least 1. Sending 0 or a negative number must be rejected with a 400 error.

If the product being added does not exist, the server returns a 404 error. If the quantity asked for is more than what is in stock, the server returns a 400 error.

If the same product is added to the cart more than once, the quantities are added together. The existing cart quantity is not replaced.

When updating a cart item, the new quantity must also be at least 1.

When removing an item, if the product is not in the cart, the server returns a 404 error.

Each item in the cart must show the correct subtotal, which is the quantity times the unit price.

The cart total must be the sum of all item subtotals. Every item must be counted, including the last one.

---

## Coupons

APIs: `POST /api/v1/coupon/apply`, `POST /api/v1/coupon/remove`

The user can apply a coupon code or remove it.

When applying a coupon, the system must check four things. First, the coupon must not be expired. Second, the cart total must meet the coupon's minimum cart value. Third, the discount must be calculated correctly. A PERCENT coupon takes a percentage off the total, and a FIXED coupon takes a flat amount off. Fourth, if the coupon has a maximum discount cap, the discount must not go above that cap.

---

## Checkout

API: `POST /api/v1/checkout`

Note: The field for JSON is "payment_method"

The user can check out using COD, WALLET, or CARD. Any other payment method is rejected with a 400 error.

The cart must not be empty. If it is empty, the server returns a 400 error.

The total is calculated correctly with no number overflow. GST is 5 percent and is added only once.

COD is not allowed if the order total is more than 5000. If someone tries, the server returns a 400 error.

When paying with COD or WALLET, the order starts with a payment status of PENDING. When paying with CARD, it starts as PAID.

---

## Wallet

APIs: `GET /api/v1/wallet`, `POST /api/v1/wallet/add`, `POST /api/v1/wallet/pay`

The user can view their balance, add money, and pay from the wallet.

When adding money, the amount must be more than 0 and at most 100000.

When paying from the wallet, the amount must be more than 0. If the wallet balance is not enough to cover the payment, the server returns a 400 error.

When paying from the wallet, the exact amount requested is deducted from the balance. No extra amount is taken.

---

## Loyalty Points

APIs: `GET /api/v1/loyalty`, `POST /api/v1/loyalty/redeem`

The user can view their loyalty points and redeem them.

When redeeming, the user must have enough points. The amount to redeem must be at least 1.

---

## Orders

APIs: `GET /api/v1/orders`, `GET /api/v1/orders/{order_id}`, `POST /api/v1/orders/{order_id}/cancel`, `GET /api/v1/orders/{order_id}/invoice`

The user can view all their orders, view one order in detail, cancel an order, and get an invoice.

A delivered order cannot be cancelled. If someone tries, the server returns a 400 error. Trying to cancel an order that does not exist returns a 404 error.

When an order is cancelled, all the items in that order are added back to the product stock.

The invoice shows the subtotal, the GST amount, and the total. The subtotal is the total before GST. The total shown must match the actual order total exactly.

---

## Reviews

APIs: `GET /api/v1/products/{product_id}/reviews`, `POST /api/v1/products/{product_id}/reviews`

The user can view reviews for a product and add a new review.

A review rating must be between 1 and 5. Anything outside that range must be rejected with a 400 error.

A comment must be between 1 and 200 characters.

The average rating shown must be a proper decimal calculation, not a rounded-down integer. If a product has no reviews yet, the average rating is 0.

---

## Support Tickets

APIs: `POST /api/v1/support/ticket`, `GET /api/v1/support/tickets`, `PUT /api/v1/support/tickets/{ticket_id}`

The user can create a support ticket, view all tickets, and update a ticket's status.

When creating a ticket, the subject must be between 5 and 100 characters. The message must be between 1 and 500 characters. The full message must be saved exactly as written.

A new ticket always starts with status OPEN.

Status can only move in one direction. OPEN can go to IN_PROGRESS. IN_PROGRESS can go to CLOSED. No other changes are allowed.
