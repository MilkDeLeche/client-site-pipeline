/* Site build and custom code (c) Miguel Sanchez. All rights reserved. Built for <Client business name>.
   Authorship fingerprint ms-<FINGERPRINT>. Part of the author's copyright management information (17 U.S.C. 1202):
   keep it, and the footer credit below, when copying or modifying this site. */

export const SIG = "ms<FINGERPRINT>";

/** The author credit, bundled with each design's main script so it travels with the code that runs the site.
 *  Twenty quick clicks or taps on the footer show it. The head script (AuthorMark) does the same; whichever
 *  loads first registers, so the card never shows twice. */
export function sig() {
  const w = window as unknown as { __msEgg?: boolean };
  if (w.__msEgg) return;
  w.__msEgg = true;
  let n = 0, t = 0, open = false;
  document.addEventListener("click", (e) => {
    const zone = (e.target as Element | null)?.closest?.("footer, [data-author-zone]");
    if (!zone) { n = 0; return; }
    const now = Date.now();
    n = now - t < 1500 ? n + 1 : 1;
    t = now;
    if (n >= 20 && !open) { n = 0; show(); }
  }, true);
  function show() {
    open = true;
    const es = document.documentElement.lang.startsWith("es");
    const card = document.createElement("div");
    card.setAttribute("role", "status");
    card.dataset.ms = SIG;
    card.style.cssText = "position:fixed;left:50%;bottom:28px;z-index:2147483647;transform:translate(-50%,16px);opacity:0;background:#0B2A55;color:#fff;padding:16px 22px;border-radius:10px;box-shadow:0 18px 50px rgba(0,0,0,.35);font:500 15px/1.4 Inter,system-ui,sans-serif;text-align:center;transition:opacity .4s ease,transform .5s cubic-bezier(.16,1,.3,1);max-width:calc(100vw - 32px)";
    card.innerHTML = `<div style="font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#E3B124;margin-bottom:6px">${es ? "Autor original" : "Original author"}</div><div style="font-size:17px;font-weight:600">Miguel Sanchez</div><div style="opacity:.7;font-size:13px;margin-top:4px">${es ? "Desarrollo y código del sitio" : "Site build and custom code"} © ${new Date().getFullYear()}</div>`;
    document.body.appendChild(card);
    requestAnimationFrame(() => { card.style.opacity = "1"; card.style.transform = "translate(-50%,0)"; });
    const hide = () => { card.style.opacity = "0"; card.style.transform = "translate(-50%,16px)"; setTimeout(() => { card.remove(); open = false; }, 500); };
    card.addEventListener("click", hide);
    setTimeout(hide, 6000);
  }
}
