import type { Rich } from "@/lib/copy";

/** Renders a Rich copy array: plain text, gradient-italic `em`, highlight-bar text. */
export function RichText({ value }: { value: Rich }) {
  return (
    <>
      {value.map((seg, i) => {
        if (seg.em) {
          return (
            <em key={i} className="font-display italic grad-text">
              {seg.text}
            </em>
          );
        }
        if (seg.highlight) {
          return (
            <span key={i} className="highlight-bar">
              {seg.text}
            </span>
          );
        }
        return <span key={i}>{seg.text}</span>;
      })}
    </>
  );
}
