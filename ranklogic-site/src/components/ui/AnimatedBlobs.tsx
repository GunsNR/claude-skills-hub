/** Fixed background layer: CSS-animated gradient blobs + grain overlay. */
export function AnimatedBlobs() {
  return (
    <>
      <div className="blob-layer" aria-hidden>
        <div className="blob blob-1" />
        <div className="blob blob-2" />
        <div className="blob blob-3" />
        <div className="blob blob-4" />
      </div>
      <div className="grain" aria-hidden />
    </>
  );
}
