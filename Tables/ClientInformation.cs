using System.ComponentModel.DataAnnotations;

namespace proj4353.Tables
{
    public class ClientInformation
    {
        [Key]
        public string Name { get; set; }

        public string CompanyName { get; set; }

        [DataType(DataType.ContactInfo)]
        public string ContactInfo { get; set; }

        [DataType(DataType.Address)]
        public string Address { get; set; }

    }
}
