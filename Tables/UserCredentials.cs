using System.ComponentModel.DataAnnotations;

namespace proj4353.Tables
{
    public class UserCredentials
    {
        [Key]
        public int ID { get; set; }

        [DataType(DataType.Password)]
        public string Password { get; set; }

    }
}
