# anime777.js
Web-API for [anime777.ru](https://anime777.ru) russian website to read manga, ranobe and watch anime together

## Example
```JavaScript
async function main() {
	const { Anime777 } = require("./anime777.js")
	const anime777 = new Anime777()
	await anime777.loginWithConnectSid("connectSid")
}

main()
```
