/**
 * SKOTE SAAS DASHBOARD THEME - CHART WIDGETS (charts.js)
 * Render interactive Chart.js widgets for revenue, traffic, and SaaS growth.
 */

document.addEventListener('DOMContentLoaded', () => {
  initEarningsChart();
  initTrafficChart();
});

function initEarningsChart() {
  const ctx = document.getElementById('earningsChart');
  if (!ctx || typeof Chart === 'undefined') return;

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
      datasets: [
        {
          label: 'Ingresos 2026 ($)',
          data: [18000, 24000, 22000, 31000, 29000, 35000, 42000, 39000, 48000, 52000, 58000, 64000],
          backgroundColor: '#556ee6',
          borderRadius: 4,
          borderSkipped: false,
        },
        {
          label: 'Gastos 2026 ($)',
          data: [8000, 11000, 9500, 14000, 12000, 15000, 18000, 16000, 21000, 22000, 24000, 26000],
          backgroundColor: '#eff2f7',
          borderRadius: 4,
          borderSkipped: false,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: {
            usePointStyle: true,
            boxWidth: 8,
            font: { family: 'Inter', size: 12 }
          }
        }
      },
      scales: {
        x: {
          grid: { display: false }
        },
        y: {
          grid: { color: 'rgba(0,0,0,0.05)' }
        }
      }
    }
  });
}

function initTrafficChart() {
  const ctx = document.getElementById('trafficChart');
  if (!ctx || typeof Chart === 'undefined') return;

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Directo', 'Redes Sociales', 'Referidos', 'Búsqueda Orgánica'],
      datasets: [{
        data: [45, 25, 18, 12],
        backgroundColor: ['#556ee6', '#34c38f', '#f1b44c', '#50a5f1'],
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            usePointStyle: true,
            boxWidth: 8,
            font: { family: 'Inter', size: 11 }
          }
        }
      },
      cutout: '70%'
    }
  });
}
