# Kilometrówka in python
Python script that generates csv file for evidence how many km tax payer did to earn an income 

## Configuration
For validt file format you have to input your name and surname, address, registration plate, engine capacity, how many km you drive every day (forth and back), and price per 1 km (according for Polish law it's 0.8358 for cars with engines > 900 cm^3)

Content of config.json
`{
	"name":"obfuscated",
	"address":"obfuscated",
	"registration_plate":"obfuscated",
	"engine_capacity": "1998cm3",
	"km":"12",
	"1km_price":"0.8358"
}
`