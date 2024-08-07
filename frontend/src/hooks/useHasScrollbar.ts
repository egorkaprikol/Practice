import { useEffect, useState, RefObject } from "react";

function useHasScrollbar(ref: RefObject<HTMLElement>): boolean {
  const [hasScrollbar, setHasScrollbar] = useState(false);

  useEffect(() => {
    const checkForScrollbar = () => {
      if (ref.current) {
        const hasScroll = ref.current.scrollHeight > ref.current.clientHeight;
        setHasScrollbar(hasScroll);
      }
    };

    checkForScrollbar();
    window.addEventListener("resize", checkForScrollbar);
    return () => window.removeEventListener("resize", checkForScrollbar);
  }, [ref]);

  return hasScrollbar;
}

export default useHasScrollbar;
