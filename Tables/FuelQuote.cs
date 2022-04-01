using System.ComponentModel.DataAnnotations;

namespace proj4353.Tables
{
    public class FuelQuote
    {
        [Key]
        public string Customer { get; set; } //Needs to be a Foreign Key from "ClientInformation" table

        public int GallonsReq { get; set; }

        public DateTime DeliveryDate { get; set; }

        public float SuggestedPrice { get; set; }

        public float AmountDue { get; set; }

    }
}
