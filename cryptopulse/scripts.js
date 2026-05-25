// Simple chart initializers for CryptoPulse demo pages
document.addEventListener('DOMContentLoaded', function () {
  // Market trend line
  const marketCtx = document.getElementById('marketTrendChart');
  if (marketCtx) {
    new Chart(marketCtx.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
        datasets: [{
          label: 'Market Index',
          data: [120, 125, 123, 130, 135, 140, 138],
          borderColor: 'rgba(92,177,255,0.95)',
          backgroundColor: 'rgba(92,177,255,0.12)',
          fill: true,
          tension: 0.3
        }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  // Allocation pie
  const alloc = document.getElementById('allocationChart');
  if (alloc) {
    new Chart(alloc.getContext('2d'), {
      type: 'doughnut',
      data: {
        labels: ['BTC','ETH','SOL','ADA','Other'],
        datasets: [{
          data: [45,28,14,8,5],
          backgroundColor: ['#f59e0b','#60a5fa','#a855f7','#22d3ee','#94a3c4']
        }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  // Portfolio allocation small
  const portfolioAlloc = document.getElementById('portfolioAllocation');
  if (portfolioAlloc) {
    new Chart(portfolioAlloc.getContext('2d'), {
      type: 'pie',
      data: {
        labels: ['Bitcoin','Ethereum','Solana','Cardano'],
        datasets: [{
          data: [45,28,14,13],
          backgroundColor: ['#f59e0b','#60a5fa','#a855f7','#22d3ee']
        }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }

  // Sentiment bar
  const sentiment = document.getElementById('sentimentChart');
  if (sentiment) {
    new Chart(sentiment.getContext('2d'), {
      type: 'bar',
      data: {
        labels: ['Bullish','Neutral','Bearish'],
        datasets: [{
          label: 'Sentiment',
          data: [68,21,11],
          backgroundColor: ['#34d399','#60a5fa','#f87171']
        }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }
});
