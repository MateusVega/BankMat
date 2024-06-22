<h1>Mateus Bank - Simple Banking System</h1>
<p>Welcome to Mateus Bank, a simple command-line banking system that allows users to register, log in, check their balance, deposit and withdraw funds, and view their transaction history. This README will guide you through the setup and usage of the system.</p>

<h2>Features</h2>
<ul>
    <li>User Registration</li>
    <li>User Login</li>
    <li>Check Balance</li>
    <li>Deposit Funds</li>
    <li>Withdraw Funds</li>
    <li>View Transaction History</li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>sqlite3</code> library (bundled with Python standard library)</li>
    <li><code>os</code> library (bundled with Python standard library)</li>
    <li><code>uuid</code> library (bundled with Python standard library)</li>
    <li><code>datetime</code> library (bundled with Python standard library)</li>
    <li><code>time</code> library (bundled with Python standard library)</li>
</ul>

<h2>Getting Started</h2>
<h3>Setting up the Database</h3>
<p>Before running the program, you need to set up the SQLite database. Uncomment the lines in the code where the tables are created:</p>
<pre><code># cursor_contas.execute('''create table contas(nome text, senha text, account text, saldo real)''')
# cursor_contas.execute('''create table transacao(nome, senha, valor real, tipo text, dia text)''')</code></pre>
<p>Run the script once to create the necessary tables. After the tables are created, you can comment these lines again to prevent recreating the tables on every run.</p>

<h3>Running the Program</h3>
<p>To run the program, execute the script:</p>
<pre><code>python mateus_bank.py</code></pre>

<h3>Usage</h3>
<ol>
    <li><strong>Main Menu</strong>: After running the script, you will be prompted to choose whether to register, log in, or exit.</li>
    <li><strong>Register</strong>: If you choose to register, you will need to provide a new username and password.</li>
    <li><strong>Log In</strong>: If you choose to log in, you will need to provide your registered username and password.</li>
    <li><strong>Banking Options</strong>: Once logged in, you can choose from the following options:
        <ul>
            <li>Check Balance</li>
            <li>Deposit Funds</li>
            <li>Withdraw Funds</li>
            <li>View Transaction History</li>
            <li>Exit</li>
        </ul>
    </li>
</ol>

<h3>Code Overview</h3>
<h4>Functions</h4>
<ul>
    <li><code>pergunta_reg_ou_log()</code>: Displays the main menu and handles user input for registration, login, or exit.</li>
    <li><code>header()</code>: Clears the screen and displays the Mateus Bank header.</li>
    <li><code>registrar()</code>: Handles user registration and stores the new user information in the database.</li>
    <li><code>logar()</code>: Handles user login and verifies the user credentials.</li>
    <li><code>bank(name, senha)</code>: Displays the banking options menu and handles user input for various banking operations.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this repository and submit pull requests if you have any improvements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

<hr>
<p>Thank you for using Mateus Bank! If you have any questions or issues, please feel free to contact us.</p>
