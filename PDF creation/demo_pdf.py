from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()
html = HTML(string='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billing Page</title>
    <style>

        /* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
}

header {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

main {
    display: flex;
    justify-content: space-between;
    padding: 20px;
}

.billing-details {
    flex: 1;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.billing-details h2 {
    margin-top: 0;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-top: 10px;
}

input,
textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #555;
}

.order-summary {
    flex: 1;
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.order-summary h2 {
    margin-top: 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

footer {
    text-align: center;
    background-color: #333;
    color: #fff;
    padding: 1rem 0;
}


    </style>
</head>
<body>
    <header>
        <h1>Billing Information</h1>
    </header>
    <main>
        <section class="billing-details">
            <h2>Billing Details</h2>
            <form>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="address">Address:</label>
                <textarea id="address" name="address" required></textarea>

                <label for="card-number">Card Number:</label>
                <input type="text" id="card-number" name="card-number" required>

                <label for="expiry-date">Expiry Date:</label>
                <input type="text" id="expiry-date" name="expiry-date" placeholder="MM/YY" required>

                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" required>

                <button type="submit">Pay Now</button>
            </form>
        </section>
        <section class="order-summary">
            <h2>Order Summary</h2>
            <ul>
                <li>Product 1: $10.00</li>
                <li>Product 2: $20.00</li>
                <li>Shipping: $5.00</li>
            </ul>
            <p>Total: $35.00</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Your Company Name</p>
    </footer>
</body>
</html>

'''
)
css = CSS(string='''
    @font-face {
          
    
        font-family: Gentium;
        src: url(http://example.com/fonts/Gentium.otf);
    

    }
    h1 { font-family: Gentium; } 
    
    
          
    ''', font_config=font_config)
html.write_pdf(
    './example.pdf', stylesheets=[css],
    font_config=font_config)