// Flat illustrations for the blog graphics (featured images and pins). Each function returns an SVG with
// viewBox 0 0 400 400; the template puts it on a colored circle. Brand and food colors only.
(function () {
  const svg = (body) => `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
  const shadow = (cx, cy, rx) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${rx * 0.14}" fill="#101614" opacity=".08"/>`;
  const leaf = (x, y, rot, s, c = '#6FA864') =>
    `<g transform="translate(${x},${y}) rotate(${rot}) scale(${s})"><path d="M0,-30 C20,-20 20,20 0,30 C-20,20 -20,-20 0,-30Z" fill="${c}"/><path d="M0,-26 L0,26" stroke="#4E8A47" stroke-width="2.5"/></g>`;
  const broccoli = (x, y, s) => {
    const pts = [[-18, -4, 14], [0, -14, 16], [18, -4, 14], [-9, 9, 12], [9, 9, 12]];
    return `<g transform="translate(${x},${y}) scale(${s})"><path d="M-6,8 L-4,34 Q0,38 4,34 L6,8Z" fill="#A9CB8E"/>` +
      pts.map(([a, b, r]) => `<circle cx="${a}" cy="${b}" r="${r}" fill="#4F8A57"/><circle cx="${a - r * .25}" cy="${b - r * .3}" r="${r * .5}" fill="#6AA56F"/>`).join('') + '</g>';
  };
  const berry = (x, y, r, c = '#4B5FA8') => `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}"/><circle cx="${x - r * .3}" cy="${y - r * .3}" r="${r * .3}" fill="#fff" opacity=".35"/>`;
  const strawberry = (x, y, s) => `<g transform="translate(${x},${y}) scale(${s})"><path d="M0,30 C-26,14 -26,-14 -14,-20 C-6,-24 6,-24 14,-20 C26,-14 26,14 0,30Z" fill="#E0483A"/><path d="M-14,-20 L-6,-30 L0,-22 L6,-30 L14,-20 L0,-16Z" fill="#5E9C4E"/>${[[-8, -4], [6, -6], [-2, 8], [10, 6], [-10, 10]].map(([a, b]) => `<ellipse cx="${a}" cy="${b}" rx="1.6" ry="2.4" fill="#FBD9A0"/>`).join('')}</g>`;
  const steam = (x, y) => `<path d="M${x},${y} c-10,-14 10,-22 0,-38 M${x + 22},${y + 4} c-10,-14 10,-22 0,-38" fill="none" stroke="#C9C6BC" stroke-width="6" stroke-linecap="round"/>`;

  window.ICONS = {
    breakfast: () => svg(shadow(200, 330, 150) +
      `<circle cx="200" cy="215" r="135" fill="#FFFFFF"/><circle cx="200" cy="215" r="112" fill="#F9F8F4"/>` +
      `<rect x="96" y="150" width="104" height="110" rx="26" fill="#C98E47"/><rect x="106" y="160" width="84" height="90" rx="20" fill="#EFCB8E"/>` +
      `<path d="M210,170 C250,140 310,165 305,215 C300,262 240,275 214,250 C188,228 180,192 210,170Z" fill="#FFFFFF" stroke="#EDEAE2" stroke-width="3"/>` +
      `<circle cx="252" cy="212" r="28" fill="#F6B732"/><circle cx="244" cy="204" r="9" fill="#FCD877"/>` +
      `<ellipse cx="175" cy="290" rx="34" ry="20" fill="#5E8F3E"/><ellipse cx="175" cy="290" rx="24" ry="13" fill="#C8DB86"/><circle cx="182" cy="292" r="8" fill="#8A5A2B"/>` +
      berry(250, 290, 9) + berry(268, 280, 9) + berry(264, 300, 8)),

    water: () => svg(shadow(200, 352, 110) +
      `<path d="M120,60 L280,60 L262,330 Q260,345 245,345 L155,345 Q140,345 138,330Z" fill="#FFFFFF" stroke="#C9D6DA" stroke-width="5"/>` +
      `<path d="M128,140 L272,140 L262,328 Q261,336 252,336 L148,336 Q139,336 138,328Z" fill="#BFE0EA"/>` +
      `<path d="M128,140 Q165,128 200,140 T272,140" fill="none" stroke="#E4F3F7" stroke-width="6"/>` +
      `<path d="M150,160 L158,310" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".8"/>` +
      `<g transform="translate(232,105) rotate(20)"><circle r="46" fill="#F2CF4A"/><circle r="39" fill="#FBEA9A"/>${[0, 1, 2, 3, 4, 5, 6, 7].map(i => { const a = i * Math.PI / 4; return `<path d="M0,0 L${Math.cos(a - .32) * 34},${Math.sin(a - .32) * 34} A34,34 0 0 1 ${Math.cos(a + .32) * 34},${Math.sin(a + .32) * 34}Z" fill="#F7DC6A"/>`; }).join('')}</g>` +
      leaf(186, 190, -20, 1.2, '#7DB36A') +
      `<path d="M70,200 C70,200 52,226 52,238 a18,18 0 0 0 36,0 C88,226 70,200 70,200Z" fill="#8CCBDD"/><path d="M330,240 C330,240 316,260 316,269 a14,14 0 0 0 28,0 C344,260 330,240 330,240Z" fill="#8CCBDD"/>`),

    walking: () => svg(shadow(200, 300, 150) +
      `<path d="M70,250 C70,215 100,190 140,180 L200,165 C215,140 240,120 270,128 L300,140 C318,148 322,170 318,190 L314,250 Z" fill="#1D5A48"/>` +
      `<path d="M200,165 C215,140 240,120 270,128 L300,140 C318,148 322,170 318,190 L250,190 C230,190 212,182 200,165Z" fill="#2E7A63"/>` +
      `<path d="M60,250 L330,250 Q338,250 338,262 L336,272 Q334,284 320,284 L78,284 Q60,284 58,268Z" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="4"/>` +
      `<path d="M58,268 L338,268" stroke="#E3E2DB" stroke-width="4"/>` +
      [0, 1, 2, 3].map(i => `<path d="M${215 + i * 18},${150 + i * 3} l14,8" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>`).join('') +
      `<path d="M100,215 L150,205" stroke="#F6B732" stroke-width="10" stroke-linecap="round"/>` +
      [0, 1, 2].map(i => `<ellipse cx="${80 + i * 50}" cy="${330 + (i % 2) * 18}" rx="14" ry="8" fill="#C9C6BC"/>`).join('')),

    snacks: () => svg(shadow(200, 330, 150) +
      `<path d="M80,210 L320,210 C318,280 270,320 200,320 C130,320 82,280 80,210Z" fill="#1D5A48"/><path d="M80,210 L320,210 C318,226 300,232 200,232 C100,232 82,226 80,210Z" fill="#2E7A63"/>` +
      [[120, 196], [150, 186], [182, 194], [212, 182], [242, 192], [272, 186], [140, 206], [200, 204], [258, 206], [296, 200]].map(([x, y], i) =>
        `<ellipse cx="${x}" cy="${y}" rx="17" ry="11" transform="rotate(${i * 37} ${x} ${y})" fill="${i % 3 === 0 ? '#C98E47' : i % 3 === 1 ? '#E0B070' : '#A86F33'}"/>`).join('') +
      `<g transform="translate(280,110)"><circle r="54" fill="#E0483A"/><circle cx="-18" cy="-16" r="14" fill="#F07A68" opacity=".7"/><path d="M0,-54 C2,-70 8,-80 16,-86" stroke="#7A4E2A" stroke-width="7" stroke-linecap="round" fill="none"/>${leaf(26, -74, 60, .8)}</g>` +
      strawberry(120, 120, 1.3)),

    mealprep: () => svg(shadow(200, 345, 160) +
      `<rect x="50" y="200" width="300" height="130" rx="22" fill="#FFFFFF" stroke="#C9D6DA" stroke-width="5"/>` +
      `<rect x="62" y="212" width="140" height="106" rx="14" fill="#F5EAD0"/>` + [...Array(26)].map((_, i) => `<ellipse cx="${78 + (i % 7) * 18}" cy="${228 + Math.floor(i / 7) * 22}" rx="7" ry="3.5" transform="rotate(${(i * 47) % 180} ${78 + (i % 7) * 18} ${228 + Math.floor(i / 7) * 22})" fill="#FFFFFF"/>`).join('') +
      `<rect x="212" y="212" width="126" height="48" rx="12" fill="#DCEBDB"/>` + broccoli(245, 232, .8) + broccoli(300, 232, .8) +
      `<rect x="212" y="268" width="126" height="50" rx="12" fill="#F8E1D6"/><rect x="228" y="276" width="94" height="34" rx="12" fill="#D9914F"/><path d="M240,284 l18,18 M262,282 l18,18 M284,282 l18,18" stroke="#B66D33" stroke-width="5" stroke-linecap="round"/>` +
      `<rect x="70" y="80" width="260" height="100" rx="20" fill="#FFFFFF" stroke="#C9D6DA" stroke-width="5"/><rect x="82" y="92" width="236" height="76" rx="12" fill="#DCEBDB"/>` +
      leaf(130, 130, 40, 1) + leaf(170, 125, -30, 1.1) + `<circle cx="215" cy="130" r="16" fill="#E0483A"/><circle cx="250" cy="122" r="14" fill="#E0483A"/>` + leaf(285, 132, 70, 1) +
      `<rect x="70" y="72" width="260" height="16" rx="8" fill="#1D5A48"/><rect x="50" y="192" width="300" height="16" rx="8" fill="#1D5A48"/>`),

    latenight: () => svg(
      `<path d="M250,70 A120,120 0 1 0 330,250 A100,100 0 1 1 250,70Z" fill="#F6D776"/>` +
      [[90, 90, 6], [130, 50, 4], [340, 110, 5], [60, 180, 4], [320, 60, 3]].map(([x, y, r]) => `<path d="M${x},${y - r * 2} L${x + r * .6},${y - r * .6} L${x + r * 2},${y} L${x + r * .6},${y + r * .6} L${x},${y + r * 2} L${x - r * .6},${y + r * .6} L${x - r * 2},${y} L${x - r * .6},${y - r * .6}Z" fill="#FFFFFF"/>`).join('') +
      shadow(170, 345, 110) +
      `<defs><mask id="lmp-bite"><rect width="400" height="400" fill="#fff"/><circle cx="262" cy="196" r="30" fill="#000"/><circle cx="252" cy="244" r="24" fill="#000"/></mask></defs>` +
      `<g mask="url(#lmp-bite)"><circle cx="170" cy="230" r="90" fill="#D9A55B"/><circle cx="150" cy="210" r="60" fill="#E2B36E" opacity=".5"/>` +
      [[130, 200], [175, 175], [150, 260], [200, 230], [120, 245], [215, 285], [165, 300]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="11" ry="8" fill="#5A3A22"/>`).join('') + `</g>`),

    workout: () => svg(shadow(200, 330, 160) +
      `<rect x="40" y="250" width="320" height="56" rx="28" fill="#2E7A63"/><circle cx="332" cy="278" r="28" fill="#1D5A48"/><circle cx="332" cy="278" r="14" fill="#2E7A63"/>` +
      `<rect x="120" y="174" width="160" height="22" rx="11" fill="#9AA3A0"/>` +
      `<rect x="70" y="128" width="40" height="114" rx="14" fill="#101614"/><rect x="104" y="146" width="26" height="78" rx="10" fill="#414B46"/>` +
      `<rect x="290" y="128" width="40" height="114" rx="14" fill="#101614"/><rect x="270" y="146" width="26" height="78" rx="10" fill="#414B46"/>` +
      `<path d="M82,140 L82,230" stroke="#5D6762" stroke-width="5" stroke-linecap="round" opacity=".6"/><path d="M302,140 L302,230" stroke="#5D6762" stroke-width="5" stroke-linecap="round" opacity=".6"/>` +
      `<g transform="translate(300,80)"><path d="M0,-40 C0,-40 -26,-6 -26,10 a26,26 0 0 0 52,0 C26,-6 0,-40 0,-40Z" fill="#8CCBDD"/></g>`),

    sleep: () => svg(shadow(200, 345, 150) +
      `<path d="M60,250 C60,214 90,200 200,200 C310,200 340,214 340,250 C340,290 310,310 200,310 C90,310 60,290 60,250Z" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="5"/>` +
      `<path d="M90,232 C120,250 280,250 310,232" fill="none" stroke="#ECE9E0" stroke-width="5"/>` +
      `<path d="M215,60 A85,85 0 1 0 300,170 A70,70 0 1 1 215,60Z" fill="#1D5A48"/>` +
      `<text x="250" y="120" font-family="IS, sans-serif" font-weight="700" font-size="40" fill="#F6D776">z</text><text x="285" y="88" font-family="IS, sans-serif" font-weight="700" font-size="30" fill="#F6D776">z</text><text x="312" y="62" font-family="IS, sans-serif" font-weight="700" font-size="22" fill="#F6D776">z</text>` +
      [[80, 90, 5], [120, 150, 4], [330, 200, 4]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#F6D776"/>`).join('')),

    grocery: () => svg(shadow(200, 345, 150) +
      `<path d="M150,140 C150,90 250,90 250,140" fill="none" stroke="#7A4E2A" stroke-width="12" stroke-linecap="round"/>` +
      `<path d="M120,120 L140,40 L156,40 L140,120Z" fill="#6FA864"/><path d="M112,128 L146,40" stroke="#4E8A47" stroke-width="5"/>` +
      `<path d="M262,130 L300,52" stroke="#E07B2E" stroke-width="22" stroke-linecap="round"/>${leaf(302, 44, 30, .9)}${leaf(312, 54, 80, .8)}` +
      `<circle cx="200" cy="128" r="34" fill="#E0483A"/><path d="M200,96 l-6,-12 M200,96 l8,-10" stroke="#5E9C4E" stroke-width="5" stroke-linecap="round"/>` +
      broccoli(160, 128, 1.2) +
      `<path d="M70,150 L330,150 L306,320 Q304,334 290,334 L110,334 Q96,334 94,320Z" fill="#D9A55B"/>` +
      [0, 1, 2, 3].map(i => `<path d="M${84 + i * 3},${180 + i * 38} L${316 - i * 3},${180 + i * 38}" stroke="#B9843F" stroke-width="5"/>`).join('') +
      [0, 1, 2, 3, 4, 5].map(i => `<path d="M${110 + i * 36},152 L${118 + i * 32},332" stroke="#B9843F" stroke-width="5"/>`).join('') +
      `<rect x="60" y="140" width="280" height="22" rx="11" fill="#C98E47"/>`),

    tape: () => svg(shadow(200, 345, 140) +
      `<circle cx="170" cy="200" r="110" fill="#F6B732"/><circle cx="170" cy="200" r="76" fill="#FBD772"/><circle cx="170" cy="200" r="30" fill="#E09A1E"/>` +
      [...Array(24)].map((_, i) => { const a = i * Math.PI / 12; return `<path d="M${170 + Math.cos(a) * 92},${200 + Math.sin(a) * 92} L${170 + Math.cos(a) * (i % 2 ? 102 : 108)},${200 + Math.sin(a) * (i % 2 ? 102 : 108)}" stroke="#8A5A10" stroke-width="4"/>`; }).join('') +
      `<path d="M240,285 L360,285 L360,330 L230,330 Q215,330 222,312Z" fill="#F6B732"/>` +
      [0, 1, 2, 3, 4, 5].map(i => `<path d="M${250 + i * 20},285 L${250 + i * 20},${i % 2 ? 300 : 308}" stroke="#8A5A10" stroke-width="4"/>`).join('') +
      `<rect x="345" y="280" width="20" height="55" rx="5" fill="#101614"/>`),

    mindful: () => svg(shadow(200, 330, 150) +
      `<path d="M70,200 L330,200 C326,280 272,318 200,318 C128,318 74,280 70,200Z" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="5"/>` +
      leaf(120, 180, -50, 1.5) + leaf(160, 165, -15, 1.6, '#7DB36A') + leaf(205, 160, 20, 1.5) + leaf(250, 168, 50, 1.5, '#7DB36A') + leaf(285, 185, 75, 1.3) +
      `<circle cx="175" cy="188" r="18" fill="#E0483A"/><circle cx="230" cy="190" r="14" fill="#F6B732"/><circle cx="140" cy="196" r="12" fill="#E0483A"/>` +
      `<path d="M330,90 l0,190" stroke="#9AA3A0" stroke-width="10" stroke-linecap="round"/><path d="M314,90 L314,140 Q314,156 330,156 Q346,156 346,140 L346,90" fill="none" stroke="#9AA3A0" stroke-width="8" stroke-linecap="round"/>` +
      `<path d="M110,92 C110,72 140,72 140,92 C140,72 170,72 170,92 C170,115 140,130 140,130 C140,130 110,115 110,92Z" fill="#E0483A"/>`),

    scale: () => svg(shadow(200, 345, 150) +
      `<rect x="70" y="150" width="260" height="180" rx="40" fill="#FFFFFF" stroke="#D2D1C9" stroke-width="6"/>` +
      `<path d="M140,215 A60,60 0 0 1 260,215" fill="#F1EFE8" stroke="#D2D1C9" stroke-width="4"/><path d="M200,215 L228,180" stroke="#E0483A" stroke-width="6" stroke-linecap="round"/><circle cx="200" cy="215" r="8" fill="#101614"/>` +
      [0, 1, 2, 3, 4].map(i => { const a = Math.PI + i * Math.PI / 4; return `<path d="M${200 + Math.cos(a) * 52},${215 + Math.sin(a) * 52} L${200 + Math.cos(a) * 44},${215 + Math.sin(a) * 44}" stroke="#9AA3A0" stroke-width="4"/>`; }).join('') +
      `<rect x="110" y="250" width="70" height="56" rx="14" fill="#F1EFE8"/><rect x="220" y="250" width="70" height="56" rx="14" fill="#F1EFE8"/>` +
      `<circle cx="300" cy="96" r="52" fill="#1D5A48"/><text x="300" y="121" text-anchor="middle" font-family="IS, sans-serif" font-weight="700" font-size="72" fill="#FFFFFF">?</text>`),

    fiber: () => svg(shadow(200, 330, 150) +
      `<path d="M70,190 L330,190 C326,276 272,316 200,316 C128,316 74,276 70,190Z" fill="#1D5A48"/><path d="M70,190 L330,190 C328,206 300,214 200,214 C100,214 72,206 70,190Z" fill="#2E7A63"/>` +
      `<ellipse cx="200" cy="190" rx="124" ry="22" fill="#EED9A8"/>` + [...Array(22)].map((_, i) => `<ellipse cx="${100 + (i % 11) * 20}" cy="${182 + Math.floor(i / 11) * 12}" rx="8" ry="4" transform="rotate(${(i * 53) % 180} ${100 + (i % 11) * 20} ${182 + Math.floor(i / 11) * 12})" fill="#D9BF83"/>`).join('') +
      berry(150, 172, 13) + berry(172, 166, 12) + berry(160, 186, 11) + strawberry(232, 160, 1.1) + `<ellipse cx="270" cy="180" rx="26" ry="9" fill="#F3E3A0"/>` +
      `<g transform="translate(110,90)">${[[0, 0], [24, 10], [-20, 18], [8, 30], [36, -12]].map(([x, y], i) => `<ellipse cx="${x}" cy="${y}" rx="14" ry="9" transform="rotate(${i * 30} ${x} ${y})" fill="#8A3B2E"/><ellipse cx="${x - 3}" cy="${y - 2}" rx="4" ry="2" fill="#B5604F"/>`).join('')}</g>` +
      `<g transform="translate(290,90)">${[[0, 0], [-22, 14], [18, 18], [-4, 30]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="11" fill="#9CC46A"/>`).join('')}</g>`),

    swaps: () => svg(shadow(200, 330, 160) +
      `<rect x="62" y="110" width="96" height="200" rx="20" fill="#E0483A"/><rect x="62" y="110" width="96" height="26" rx="12" fill="#C9C6BC"/><rect x="62" y="284" width="96" height="26" rx="12" fill="#C9C6BC"/><rect x="74" y="170" width="72" height="70" rx="8" fill="#FFFFFF" opacity=".9"/><path d="M90,205 Q110,185 130,205" stroke="#E0483A" stroke-width="6" fill="none"/>` +
      `<path d="M178,210 L222,210" stroke="#1D5A48" stroke-width="14" stroke-linecap="round"/><path d="M210,188 L236,210 L210,232" fill="none" stroke="#1D5A48" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>` +
      `<path d="M250,110 L346,110 L334,300 Q333,312 320,312 L276,312 Q263,312 262,300Z" fill="#FFFFFF" stroke="#C9D6DA" stroke-width="5"/><path d="M256,160 L340,160 L334,298 Q333,304 326,304 L270,304 Q263,304 262,298Z" fill="#BFE0EA"/>` +
      `<g transform="translate(312,132) rotate(15)"><circle r="26" fill="#9CC46A"/><circle r="21" fill="#D7EBA8"/></g>` + leaf(282, 200, -10, .9)),

    eatingout: () => svg(shadow(200, 330, 150) +
      `<circle cx="200" cy="215" r="120" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="5"/><circle cx="200" cy="215" r="96" fill="#F9F8F4"/>` +
      `<path d="M130,215 A70,70 0 0 1 270,215 L270,222 L130,222Z" fill="#9AA3A0"/><path d="M130,215 A70,70 0 0 1 270,215" fill="#C9CFCC"/><circle cx="200" cy="140" r="12" fill="#9AA3A0"/><path d="M150,200 A52,52 0 0 1 190,160" stroke="#FFFFFF" stroke-width="8" fill="none" stroke-linecap="round" opacity=".7"/>` +
      `<rect x="120" y="222" width="160" height="14" rx="7" fill="#7E8783"/>` +
      `<path d="M50,110 L50,170 M38,110 L38,150 Q38,170 50,170 Q62,170 62,150 L62,110 M50,170 L50,320" stroke="#101614" stroke-width="9" stroke-linecap="round" fill="none"/>` +
      `<path d="M350,110 C330,140 330,190 350,200 L350,320" stroke="#101614" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M350,110 C330,140 330,190 350,200Z" fill="#101614"/>`),

    drinks: () => svg(shadow(200, 340, 160) +
      `<path d="M60,180 L190,180 L180,310 Q178,326 162,326 L88,326 Q72,326 70,310Z" fill="#FFFFFF" stroke="#D2D1C9" stroke-width="5"/><path d="M190,210 C230,210 230,270 186,272" fill="none" stroke="#D2D1C9" stroke-width="12"/>` +
      `<ellipse cx="125" cy="186" rx="60" ry="10" fill="#6B4226"/>` + steam(110, 160) +
      `<path d="M220,150 L340,150 L332,310 Q331,326 316,326 L244,326 Q229,326 228,310Z" fill="#FFFFFF" stroke="#C9D6DA" stroke-width="5"/><path d="M224,190 L336,190 L332,308 Q331,318 320,318 L240,318 Q229,318 228,308Z" fill="#E9C46A" opacity=".75"/>` +
      `<path d="M300,120 L300,170" stroke="#9AA3A0" stroke-width="3"/><rect x="288" y="168" width="26" height="30" rx="4" fill="#1D5A48"/>` + leaf(255, 240, 30, .8)),

    sugar: () => svg(shadow(200, 330, 150) +
      `<circle cx="150" cy="210" r="96" fill="#D9A55B"/><path d="M60,200 C70,140 230,140 240,200 C230,210 220,190 205,205 C190,190 175,212 160,198 C145,214 130,192 115,206 C100,192 85,214 70,200Z" fill="#F29AB4"/><circle cx="150" cy="210" r="30" fill="#F6F5F1"/>` +
      [[100, 175, 0], [130, 160, 40], [175, 168, 100], [205, 182, 20], [118, 195, 80], [190, 200, 60]].map(([x, y, r]) => `<rect x="${x}" y="${y}" width="16" height="5" rx="2.5" transform="rotate(${r} ${x} ${y})" fill="${['#FFFFFF', '#F6D776', '#8CCBDD'][r % 3]}"/>`).join('') +
      `<circle cx="150" cy="210" r="118" fill="none" stroke="#E0483A" stroke-width="14"/><path d="M68,128 L232,292" stroke="#E0483A" stroke-width="14" stroke-linecap="round"/>` +
      strawberry(300, 250, 2)),

    emotional: () => svg(shadow(200, 340, 140) +
      `<path d="M200,320 C200,320 70,240 70,150 C70,100 110,72 148,72 C176,72 192,88 200,104 C208,88 224,72 252,72 C290,72 330,100 330,150 C330,240 200,320 200,320Z" fill="#E0483A"/>` +
      `<path d="M110,130 C112,108 128,96 148,96" fill="none" stroke="#F07A68" stroke-width="10" stroke-linecap="round"/>` +
      `<g transform="translate(250,250) rotate(-30)"><rect x="-14" y="-110" width="28" height="70" rx="14" fill="#9AA3A0"/><ellipse cx="0" cy="-130" rx="30" ry="40" fill="#C9CFCC"/><ellipse cx="0" cy="-130" rx="22" ry="32" fill="#E3E7E5"/></g>`),

    plateau: () => svg(shadow(200, 345, 150) +
      `<rect x="60" y="70" width="280" height="260" rx="24" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="5"/>` +
      [0, 1, 2, 3].map(i => `<path d="M90,${120 + i * 52} L310,${120 + i * 52}" stroke="#F1EFE8" stroke-width="4"/>`).join('') +
      `<path d="M90,120 L140,160 L170,190 L230,192 L260,194 L310,270" fill="none" stroke="#1D5A48" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>` +
      `<path d="M170,190 L260,194" fill="none" stroke="#F6B732" stroke-width="12" stroke-linecap="round"/>` +
      `<path d="M290,262 L312,272 L306,248" fill="none" stroke="#1D5A48" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>` +
      [[90, 120], [140, 160], [170, 190], [230, 192], [260, 194]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="9" fill="#FFFFFF" stroke="#1D5A48" stroke-width="5"/>`).join('')),

    habits: () => svg(shadow(200, 350, 140) +
      `<rect x="85" y="60" width="230" height="280" rx="22" fill="#FFFFFF" stroke="#E3E2DB" stroke-width="5"/><rect x="150" y="44" width="100" height="34" rx="12" fill="#1D5A48"/>` +
      [0, 1, 2, 3].map(i => `<rect x="115" y="${108 + i * 56}" width="36" height="36" rx="10" fill="${i < 3 ? '#1D5A48' : '#F1EFE8'}"/>` +
        (i < 3 ? `<path d="M123,${126 + i * 56} l8,8 l14,-16" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>` : '') +
        `<rect x="166" y="${118 + i * 56}" width="${[110, 90, 120, 80][i]}" height="14" rx="7" fill="#E3E2DB"/>`).join('')),

    protein: () => svg(shadow(200, 330, 150) +
      `<circle cx="200" cy="215" r="130" fill="#FFFFFF"/><circle cx="200" cy="215" r="108" fill="#F9F8F4"/>` +
      `<path d="M120,190 C130,150 230,140 260,170 C285,195 270,240 230,250 C180,262 110,240 120,190Z" fill="#D9914F"/><path d="M135,190 l30,30 M165,175 l40,40 M200,170 l40,40" stroke="#B66D33" stroke-width="7" stroke-linecap="round"/>` +
      `<g transform="translate(250,250)"><ellipse rx="40" ry="30" fill="#FFFFFF" stroke="#EDEAE2" stroke-width="3"/><circle r="15" fill="#F6B732"/></g>` + broccoli(140, 265, 1.1)),
  };
})();
