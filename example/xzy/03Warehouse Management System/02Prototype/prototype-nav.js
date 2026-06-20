(function () {
  const routes = {
    receipt: "20260619_P001_AfterSalesReceiptWorkbench.html",
    quality: "20260619_P002_QualityInspectionWorkbench.html",
    putaway: "20260620_P003_PutawayWorkbench.html",
    exception: "20260620_P004_ExceptionWorkbench.html",
    config: "20260620_P005_WarehouseConfigWorkbench.html"
  };

  function resolveRoute(routeKey) {
    return routes[routeKey] || routeKey;
  }

  function buildUrl(routeKey, paramsText) {
    const url = new URL(resolveRoute(routeKey), window.location.href);

    if (!paramsText) {
      return url.toString();
    }

    try {
      const params = JSON.parse(paramsText);
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          url.searchParams.set(key, value);
        }
      });
    } catch (error) {
      // Ignore malformed static prototype metadata.
    }

    return url.toString();
  }

  function bindPrototypeNavigation() {
    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-go]");
      if (!trigger) return;

      event.preventDefault();
      window.location.href = buildUrl(trigger.dataset.go, trigger.dataset.params || "");
    });

    document.querySelectorAll("[data-go]").forEach((element) => {
      if (!element.style.cursor) {
        element.style.cursor = "pointer";
      }

      if (element.tagName === "A" && !element.getAttribute("href")) {
        element.setAttribute("href", resolveRoute(element.dataset.go));
      }
    });
  }

  window.PrototypeNav = {
    routes,
    go(routeKey, params) {
      const url = new URL(resolveRoute(routeKey), window.location.href);
      Object.entries(params || {}).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          url.searchParams.set(key, value);
        }
      });
      window.location.href = url.toString();
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindPrototypeNavigation);
  } else {
    bindPrototypeNavigation();
  }
})();
