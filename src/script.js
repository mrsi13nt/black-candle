const options = [
    { name: 'usage', description: 'usage: python3 black_candle.py [options] arg' },
    { name: '--data', description: 'Data string to be sent through POST (e.g. "data=1")' },
    { name: '--cookie', description: 'HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")' },
    { name: '-p, --payload', description: 'you can add custom payload' },
    { name: '-hh', description: 'run host header injection scanner' },
    { name: '--host', description: 'add custom host header (e.g. --host "www.ping.com")' },
    { name: '-js', description: 'scan all java script files of full website from api keys and more..' },
    { name: '-w', description: 'using simple WAF detector and trying to bypass it' },
    { name: '-rf', description: 'scan for reflected XSS' },
    { name: '-d', description: 'scan for DOM XSS' },
    { name: '-b', description: 'scan for blind xss' },
    { name: '-o', description: 'file to write output to' },
    { name: '-u, --url', description: 'Target URL (e.g. "http://www.site.com/vuln.php?id=1")' },
    { name: '-l, --list', description: 'target list of urls' }
]

const tableBody = document.querySelector('#options-table tbody')

options.forEach(option => {
    const row = document.createElement('tr')
    const nameCell = document.createElement('td')
    const descriptionCell = document.createElement('td')

    nameCell.textContent = option.name
    descriptionCell.textContent = option.description

    row.appendChild(nameCell)
    row.appendChild(descriptionCell)

    tableBody.appendChild(row)
})