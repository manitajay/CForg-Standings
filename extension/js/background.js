document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tab = tabs[0]
    var tabUrl = tab.url
    var arg = tabUrl.split('/')
    var options = ['contest']
    chrome.storage.sync.get('lastOrgurl', function (obj) {
      if (obj.lastOrgUrl) $('#selectedOrg').val(obj.lastOrgUrl)
    })
    if (options.includes(arg[3]) && arg[2] === 'codeforces.com') {
      $('#found').show()
      $('#notFound').hide()
    } else {
      $('#found').hide()
      $('#notFound').show()
    }
  })
})

$('#goToStandings').click(() => {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tab = tabs[0]
    var tabUrl = tab.url
    var arg = tabUrl.split('/')
    var listUrl = $('#selectedOrg').val()
    if (listUrl === null) {
      alert('Please select a Org')
    } else {
      var newUrl= 'https://codeforces.com/api/contest.standings?contestId='+arg[4]+'&from=1&showUnofficial=false'
      
      chrome.storage.sync.set({ lastOrgUrl: listUrl })
      chrome.tabs.update(tab.id, { url: newUrl })
    }
  })
})
