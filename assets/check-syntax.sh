#!/bin/bash
# extract <script> blocks from vault-live.html and node --check each
cd "$(dirname "$0")/.."
export PATH="$HOME/.hermes/node/bin:$PATH"
node -e '
const fs=require("fs"); const html=fs.readFileSync("vault-live.html","utf8");
const re=/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/g; let m,n=0,bad=0;
while((m=re.exec(html))){ n++; const f="/tmp/_vl_script_"+n+".js"; fs.writeFileSync(f,m[1]);
  const r=require("child_process").spawnSync(process.execPath,["--check",f],{encoding:"utf8"});
  if(r.status!==0){ bad++; const line=html.slice(0,m.index).split("\n").length; console.log("SCRIPT #"+n+" (starts html line "+line+") FAIL:\n"+r.stderr.split("\n").slice(0,6).join("\n")); } }
console.log(bad?("syntax: "+bad+" bad of "+n):("syntax OK — "+n+" script blocks"));
process.exit(bad?1:0);'
