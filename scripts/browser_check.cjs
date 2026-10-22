const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const errors=[];const results=[];
 const routes=['/','/research/','/projects/','/about/','/posts/','/blog/Welcome-website/','/categories/','/tags/','/404.html'];
 fs.mkdirSync('docs/screenshots',{recursive:true});
 for(const width of [1440,768,390,320]){
  const page=await browser.newPage({viewport:{width,height:1000},deviceScaleFactor:1});
  page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400) errors.push(`${r.status()} ${r.url()}`)});
  for(const route of routes){
   await page.goto('http://127.0.0.1:4000'+route,{waitUntil:'networkidle'});
   const result=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,images:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),h1:document.querySelector('h1')?.textContent}));
   if(result.overflow||result.images.length)errors.push({width,route,...result});
   results.push({width,route,...result});
   if([1440,768,390].includes(width)&&['/','/research/','/projects/','/blog/Welcome-website/'].includes(route))await page.screenshot({path:`docs/screenshots/${route==='/'?'home':route.split('/').filter(Boolean).pop()}-${width}.png`,fullPage:true});
  }
  await page.goto('http://127.0.0.1:4000/');
  await page.keyboard.press('Tab');
  if(await page.locator(':focus').textContent()!=='Skip to content')errors.push('Skip link not first focus target');
  await page.keyboard.press('Enter');
  if(await page.locator(':focus').getAttribute('id')!=='main')errors.push('Skip link did not focus main');
  for(const name of ['Research','Projects','Me']){
   await page.getByRole('navigation').getByRole('link',{name,exact:true}).click();
   if(await page.getByRole('navigation').locator('[aria-current="page"]').textContent()!==name)errors.push('Active navigation failure '+name);
  }
  await page.close();
 }
 await browser.close();
 fs.writeFileSync('docs/browser-results.json',JSON.stringify({results,errors},null,2));
 console.log(JSON.stringify({pagesChecked:results.length,errors},null,2));
 if(errors.length)process.exit(1);
})();
