document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.progress-bar[data-width]').forEach((bar) => {
    const width = Number(bar.dataset.width || 0);
    requestAnimationFrame(() => {
      bar.style.width = `${Math.max(0, Math.min(width, 100))}%`;
    });
  });

  document.querySelectorAll('canvas[data-chart-config]').forEach((canvas) => {
    const config = canvas.dataset.chartConfig;
    if (!config || typeof Chart === 'undefined') {
      return;
    }

    try {
      const parsed = JSON.parse(config);
      new Chart(canvas, parsed);
    } catch (error) {
      console.error('Failed to initialize chart', error);
    }
  });
});
