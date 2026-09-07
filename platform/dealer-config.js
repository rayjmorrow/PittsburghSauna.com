// Dealer-level configuration for the shared dealer growth platform.
window.DEALER_PLATFORM = window.DEALER_PLATFORM || {};
window.DEALER_PLATFORM.dealer = {
  id: "htfo",
  siteId: "pittsburgh-sauna",
  name: "Hot Tub Factory Outlet",
  market: "Greater Pittsburgh",
  phone: "412-326-0361",
  locations: [
    { id: "monroeville", name: "Monroeville", address: "4680 Old William Penn Hwy, Monroeville, PA 15146" },
    { id: "wexford", name: "Wexford", address: "10269 Perry Hwy, Wexford, PA 15090" }
  ],
  assistant: { enabled: true, name: "Bubbles", preserveBrandName: true },
  crm: { provider: null, endpoint: null },
  attribution: { preserveUtm: true, preserveLandingPage: true, preserveReferrer: true }
};
