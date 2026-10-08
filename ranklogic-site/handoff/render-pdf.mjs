import { chromium } from "playwright";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve } from "node:path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const htmlPath = resolve(__dirname, "strategy.html");
const pdfPath = resolve(__dirname, "ranklogic-niche-brief.pdf");

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const ctx = await browser.newContext();
const page = await ctx.newPage();
await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "networkidle" });
await page.pdf({
  path: pdfPath,
  format: "Letter",
  printBackground: true,
  margin: { top: "0.6in", bottom: "0.7in", left: "0.55in", right: "0.55in" },
  displayHeaderFooter: true,
  headerTemplate: '<div></div>',
  footerTemplate: '<div style="font-size:8pt;color:#8a93a0;width:100%;padding:0 0.55in;display:flex;justify-content:space-between;font-family:-apple-system,Helvetica,Arial,sans-serif;"><span>RankLogic SEO · South Florida Impact Window Brief</span><span class="pageNumber"></span></div>',
});
await browser.close();
console.log("Wrote", pdfPath);
