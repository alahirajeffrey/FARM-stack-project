import Button from "./Button";

const Navbar = () => {
  const addMenuItem = () => {
    console.log("button in navbar clicked");
  };

  return (
    <div className="grid grid-cols-3 gap-4 bg-blue-800 py-3 ">
      <div className="col-span-2 flex items-center justify-center">
        <h1 className=" px-5 font-black text-3xl ">Sholly Restaurant Menu</h1>
      </div>
      <div className="flex justify-center items-center">
        <Button title={"Add Menu"} onClick={addMenuItem} />
      </div>
    </div>
  );
};

export default Navbar;
