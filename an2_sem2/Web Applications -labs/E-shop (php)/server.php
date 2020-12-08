<!DOCTYPE html>
<html>
<head>
<style>
table {
    width: 60%;
    border-collapse: collapse;
}

table, td, tr {
    border: 1px solid black;
    padding: 5px;
}

tr {text-align: left;}
</style>
</head>
<body>

<?php
$no_of_records_per_page=4;

$urlParams = explode('/', $_SERVER['REQUEST_URI']);
$functionName = $urlParams[3];
$functionName = explode('?', $functionName);
$functionName = $functionName[0];

$functionName();

function products () 
{
global $no_of_records_per_page;
	
$q = intval($_GET['q']);
$pageNumber = intval($_GET['pageNumber']);
$offset = ($pageNumber-1) * $no_of_records_per_page;

$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"store");
if($q==1)
	$sql="SELECT * FROM products WHERE description = 'women' LIMIT $offset, $no_of_records_per_page";
else if($q==2)
	$sql="SELECT * FROM products WHERE description = 'men' LIMIT $offset, $no_of_records_per_page";
else if($q==3)
	$sql="SELECT * FROM products LIMIT $offset, $no_of_records_per_page";

$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<td><b>id</b></td>
<td><b>name</b></td>
<td><b>price</b></td>
<td><b>description</b></td>
</tr>";
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['name'] . "</td>";
    echo "<td>" . $row['price'] . "</td>";
    echo "<td>" . $row['description'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
}

function basket () 
{
$q = intval($_GET['q']);
$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"store");
$sql="SELECT * FROM basket";

$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<td><b>id</b></td>
<td><b>product_id</b></td>
<td><b>quantity</b></td>
</tr>";
while($row = mysqli_fetch_array($result)) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['product_id'] . "</td>";
    echo "<td>" . $row['quantity'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
}

function delete () 
{
$q = intval($_GET['q']);
$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

$sql = "DELETE FROM basket WHERE id= $q";

$result = mysqli_query($con,$sql);

mysqli_close($con);
}

function update () 
{
$q = intval($_GET['q']);
$t = intval($_GET['t']);	
	
$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

$sql = "UPDATE basket SET quantity=$t WHERE id= $q";

$result = mysqli_query($con,$sql);

mysqli_close($con);
}

function add () 
{
$q = intval($_GET['q']);
$t = intval($_GET['t']);	
	
$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

$sql = "INSERT INTO basket (product_id, quantity) VALUES ($q,$t)";

$result = mysqli_query($con,$sql);

mysqli_close($con);
}

function nrOfPages()
{
	$con = mysqli_connect('localhost','root','','store');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

$sql = "SELECT COUNT(*) FROM products";

$result = mysqli_query($con,$sql);

return intval($result);
}


?>
</body>
</html>
