const FRAME_COUNT = 80;
const sequenceFrame = document.getElementById("sequenceFrame");
const heroFrame = document.getElementById("heroFrame");
const frameLabel = document.getElementById("frameLabel");
const scrolly = document.getElementById("scrolly");
const steps = [...document.querySelectorAll(".step")];

const frameSrc = (index) =>
  `./assets/frames/frame_${String(index).padStart(4, "0")}.jpg`;

const labels = [
  { until: 0.34, text: "Fragments gather" },
  { until: 0.72, text: "Signal emerges" },
  { until: 1, text: "Landing clean" },
];

const clamp = (value, min, max) => Math.min(max, Math.max(min, value));

function updateFrameFromScroll() {
  if (!scrolly || !sequenceFrame) {
    return;
  }

  const rect = scrolly.getBoundingClientRect();
  const total = scrolly.offsetHeight - window.innerHeight;
  const traveled = clamp(-rect.top, 0, total);
  const progress = total <= 0 ? 0 : traveled / total;
  const frame = clamp(Math.round(progress * (FRAME_COUNT - 1)) + 1, 1, FRAME_COUNT);

  sequenceFrame.src = frameSrc(frame);
  if (heroFrame && frame <= 8) {
    heroFrame.src = frameSrc(frame);
  }

  const label = labels.find((entry) => progress <= entry.until) || labels.at(-1);
  frameLabel.textContent = label.text;

  steps.forEach((step, index) => {
    const thresholdStart = index / steps.length;
    const thresholdEnd = (index + 1) / steps.length;
    const active = progress >= thresholdStart && progress <= thresholdEnd;
    step.style.transform = active ? "translateY(0)" : "translateY(18px)";
    step.style.opacity = active ? "1" : "0.55";
  });
}

if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  sequenceFrame.src = frameSrc(FRAME_COUNT);
  heroFrame.src = frameSrc(FRAME_COUNT);
  frameLabel.textContent = "Landing clean";
  steps.forEach((step) => {
    step.style.transform = "none";
    step.style.opacity = "1";
  });
} else {
  updateFrameFromScroll();
  document.addEventListener("scroll", updateFrameFromScroll, { passive: true });
  window.addEventListener("resize", updateFrameFromScroll);
}
