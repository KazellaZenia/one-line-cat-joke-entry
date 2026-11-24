// One-line cat joke entry for make.fun bounty
// u-aldy998-the-one-line-cat-joke-that-lands-a7b18262
// Writes a single original cat joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

const fs = require("node:fs");
const path = require("node:path");

const JOKE =
  "My cat stares at a blank wall for an hour, then looks at me like I'm the one wasting time.";

function main() {
  // Gate validation, in code, before writing anything.
  if (typeof JOKE !== "string" || JOKE.trim().length === 0) {
    throw new Error("joke must not be blank");
  }
  if (JOKE.length < 1 || JOKE.length > 200) {
    throw new Error(`joke must be 1-200 characters, got ${JOKE.length}`);
  }
  if (JOKE.includes("\n") || JOKE.includes("\r")) {
    throw new Error("joke must be a single line");
  }

  const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "entry.txt");
  fs.writeFileSync(outPath, JOKE, "utf8");

  // Verify the written file by reading it back.
  const written = fs.readFileSync(outPath, "utf8");
  if (written !== JOKE) {
    throw new Error("verification failed: entry.txt does not match the joke");
  }
  console.log(`Wrote ${JOKE.length}-character joke to ${outPath}`);
}

main();
