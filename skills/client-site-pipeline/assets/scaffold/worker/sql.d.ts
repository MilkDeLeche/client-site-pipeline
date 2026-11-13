/// <reference types="@cloudflare/workers-types" />
// Wrangler bundles *.sql as text (see "rules" in wrangler.jsonc).
declare module "*.sql" {
  const sql: string;
  export default sql;
}
